from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel,Field
import pandas as pd
import io
import joblib

app = FastAPI(title="Customer Churn Prediction API",description="An API for predicting customer churn using a pre-trained machine learning model.",version="1.0.0")

model = joblib.load("model/churn_model.pkl")
mae = joblib.load("model/mae.pkl")

class ChurnPredictionRequest(BaseModel):
    gender: str = Field(..., description="Gender of the customer (Male/Female)")
    SeniorCitizen: int = Field(..., description="Whether the customer is a senior citizen (1 for Yes, 0 for No)")
    tenure: int = Field(..., description="Number of months the customer has been with the company")
    InternetService: str = Field(..., description="Type of internet service (DSL/Fiber optic/No)")
    Contract: str = Field(..., description="Type of contract (Month-to-month/One year/Two year)")
    MonthlyCharges: float = Field(..., description="The amount charged to the customer monthly")
    TotalCharges: float = Field(..., description="The total amount charged to the customer")
    TechSupport: str = Field(..., description="Whether the customer has tech support (Yes/No)")
    PaperlessBilling: str = Field(..., description="Whether the customer has paperless billing (Yes/No)")

@app.get("/")
def hello():
    return {"message": "Welcome to the Customer Churn Prediction API"}

@app.get("/intro")
def intro():
    return {"message": "This API predicts customer churn based on input features. Please provide the required data in the request body."}

@app.get("/health") 
def health():
    return {
        "status": "running",
        "model": "RandomForestClassifier",
        "avg_error": round(float(mae), 4)
        }

@app.post("/predict")
def predict(cust: ChurnPredictionRequest):
    try:
        input_data = pd.DataFrame([cust.model_dump()])
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)[:, 1]
        return {
            "prediction": "Yes" if prediction[0] == 1 else "No",
            "probability": round(float(prediction_proba[0]), 4)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict_file")
def predict_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]
        df['Churn_Prediction'] = ["Yes" if pred == 1 else "No" for pred in predictions]
        df['Churn_Probability'] = probabilities
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=predictions.csv"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))