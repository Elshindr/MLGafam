import pytest
from dotenv import load_dotenv
import os
import pandas as pd
import joblib
import numpy as np

load_dotenv()
DATA_DIR= os.getenv("DATA_DIR", "./data/")
model = joblib.load("models/model.pkl")

@pytest.fixture 
def fichier(): 
    f = open(DATA_DIR+"prepared_people_test.csv", "w") 
    yield f 
    f.close()
    
def test_model_mae(fichier) :
    df = pd.read_csv(fichier, sep=",")
    
    X = df[["company_name", "personal_gender", "job_position_level", "job_performance_score", "job_work_hours_per_week", "experience_experience_years", "experience_has_certifications", "promoted"]]
    y = df["job_salary"]
        
    y_pred = model.predict(X)

    mae = np.mean(np.abs(y - y_pred))

    assert mae < 9000