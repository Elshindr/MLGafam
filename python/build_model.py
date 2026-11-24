from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib


load_dotenv()
DATA_DIR= os.getenv("DATA_DIR", "./data/")


if __name__ == "__main__":
    
    df = pd.read_csv(DATA_DIR+"prepared_people.csv")
    
    X = df[["company_name", "personal_gender", "job_position_level", "job_performance_score", "job_work_hours_per_week", "experience_experience_years", "experience_has_certifications", "promoted"]]
    y = df["job_salary"]
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mae = np.mean(np.abs(y_test - y_pred))
    mse = np.mean((y_test - y_pred)**2)
    rmse = np.sqrt(np.mean((y_test - y_pred)**2))
    r2 = r2_score(y_test, y_pred)
    
    joblib.dump(model, "./models/model.pkl")