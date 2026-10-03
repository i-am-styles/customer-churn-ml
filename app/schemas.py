from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    gender: str = Field(..., example="Male", description="Male / Female")
    SeniorCitizen: int = Field(..., example=0, description="0 = No, 1 = Yes")
    Partner: str = Field(..., example="Yes", description="Yes / No")
    Dependents: str = Field(..., example="No", description="Yes / No")
    tenure: int = Field(..., example=12, description="Months with company")
    PhoneService: str = Field(..., example="Yes", description="Yes / No")
    MultipleLines: str = Field(..., example="No", description="Yes / No / No phone service")
    InternetService: str = Field(..., example="DSL", description="DSL / Fiber optic / No")
    OnlineSecurity: str = Field(..., example="No", description="Yes / No / No internet service")
    OnlineBackup: str = Field(..., example="Yes", description="Yes / No / No internet service")
    DeviceProtection: str = Field(..., example="No", description="Yes / No / No internet service")
    TechSupport: str = Field(..., example="No", description="Yes / No / No internet service")
    StreamingTV: str = Field(..., example="No", description="Yes / No / No internet service")
    StreamingMovies: str = Field(..., example="No", description="Yes / No / No internet service")
    Contract: str = Field(..., example="Month-to-month", description="Month-to-month / One year / Two year")
    PaperlessBilling: str = Field(..., example="Yes", description="Yes / No")
    PaymentMethod: str = Field(..., example="Electronic check", description="Electronic check / Mailed check / Bank transfer (automatic) / Credit card (automatic)")
    MonthlyCharges: float = Field(..., example=70.5, description="Monthly bill amount")
    TotalCharges: float = Field(..., example=846.0, description="Total bill amount")

    class Config:
        json_schema_extra = {
            "example": {
                "gender": "Male",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 12,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 70.5,
                "TotalCharges": 846.0
            }
        }