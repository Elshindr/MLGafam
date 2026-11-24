from dotenv import load_dotenv
import joblib
from fastapi import FastAPI, Response, HTTPException
import os
from pydantic import BaseModel
from typing import List
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge, Summary, Histogram, CONTENT_TYPE_LATEST,generate_latest,CollectorRegistry

class Home(BaseModel):
    message:str
    
class Predictions(BaseModel):
    prediction:List[float]

class People(BaseModel):
    id:int
    gender:str
    salary:float
    company:str
    position_level:int
    score: float
    work_hours:int 
    experience_years:float
    has_certifications:bool
    promoted:bool
        
    
load_dotenv()
MODEL_PATH= os.getenv("MODEL_PATH", "../models/model.pkl")
model= joblib.load(MODEL_PATH)

app = FastAPI(title="My API",
    description="RNCP FastAPI.",
    version="1.0.1")

Instrumentator().instrument(app).expose(app)
predictions_total = Counter( "predictions_total", "Nombre total de prédictions", ["model", "status"] ) 
active_requests = Gauge( "active_requests", "Requêtes en cours de traitement" ) 
inference_duration = Histogram( "inference_duration_seconds", "Durée d'inférence", buckets=[0.01, 0.1, 0.5, 1.0] )
nb_of_requests_counter= Counter( "nombre_requete_total", "Nombre total de reque", ["method","endpoint"] ) 

@app.get("/hello", name='Home page')
def getHome() -> Home:
    nb_of_requests_counter.labels(method='GET', endpoint='/').inc()
 
    return Home(message= "Hello World!")


@app.post("/predict", name="Prediction")
def postpredict(lstPeople:List[People])->Predictions:
    active_requests.inc() 
    try:
        with inference_duration.time():
            df = pd.DataFrame([[d.model_dump() for d in lstPeople]],
            columns=["company_name", "personal_gender", "job_position_level", "job_performance_score", "job_work_hours_per_week", "experience_experience_years", "experience_has_certifications", "promoted"])            
        
            result = model.predict(df)
            predictions_total.labels(model="v1", status="success").inc() 
        return Predictions(predictions=result.tolist())

    except ValueError as e:
            predictions_total.labels(model="v1", status="error").inc() 
            raise HTTPException(
                        status_code=400,
                        detail=f"Données invalides pour l'entraînement : {e}"
                    )
    except Exception as e: 
        predictions_total.labels(model="v1", status="error").inc() 
        raise e
    
    finally: 
        active_requests.dec()