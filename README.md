# 🎯 Customer Churn Prediction API

ML model that predicts customer churn using Random Forest, deployed with FastAPI.

## 🚀 Live Demo
- **Docs:** https://your-app-name.onrender.com/docs

## 🛠️ Tech Stack
- Scikit-learn, Pandas, NumPy
- FastAPI, Pydantic, Uvicorn
- Deployed on Render

## 📁 Structure
├── app/          # FastAPI code
├── model/        # Trained model (.pkl)
├── notebooks/    # Training notebook
├── requirements.txt
└── README.md


## ⚡ Local Setup
git clone https://github.com/YOUR_USERNAME/customer-churn-ml.git
cd customer-churn-ml
python -m venv churnenv
churnenv\Scripts\activate          # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload


Open: http://127.0.0.1:8000/docs

## 📡 API Usage
**POST** /predict

**Request:**
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "tenure": 12,
  "InternetService": "DSL",
  "Contract": "Month-to-month",
  "MonthlyCharges": 70.5,
  "TotalCharges": 846.0,
  "TechSupport": "No",
  "PaperlessBilling": "Yes"
}


**Response:**
{
  "churn_prediction": "Yes",
  "churn_probability": 0.7234
}


## 📊 Model
- **Algorithm:** Random Forest
- **Accuracy:** ~75%
- **Preprocessing:** StandardScaler + OneHotEncoder

## 👤 Author
**i-am-styles** — [GitHub](https://github.com/i-am-styles)