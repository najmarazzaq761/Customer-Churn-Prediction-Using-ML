import json
import pickle
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "modelling" / "churn_prediction_model.pkl"
NOTEBOOK_PATH = BASE_DIR / "modelling" / "churn_analysis_pipeline.ipynb"

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)


def load_preprocess_function():
    with NOTEBOOK_PATH.open("r", encoding="utf-8") as notebook_file:
        notebook = json.load(notebook_file)

    namespace = {"LabelEncoder": LabelEncoder, "StandardScaler": StandardScaler}
    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))
        if "def preprocess_features" in source:
            exec(source, namespace)
            break

    if "preprocess_features" not in namespace:
        raise ValueError("preprocess_features was not found in the notebook.")

    return namespace["preprocess_features"]


preprocess_features = load_preprocess_function()

# fit preprocessing on the training dataframe once
training_df = pd.read_csv(BASE_DIR / "modelling" / "x_train.csv")
_, encoders, scaler = preprocess_features(training_df.copy(), fit=True)


def pred(user_input):
    user_df = pd.DataFrame([user_input])
    processed = preprocess_features(user_df, fit=False, encoders=encoders, scaler=scaler)
    prediction = model.predict(processed)
    return prediction[0]


st.title("Customer Churn Prediction")

category = st.text_input("category", "Hair Care")
item = st.text_input("item", "Hair Oil")
quantity = st.number_input("quantity", min_value=1, max_value=100, value=1)
price = st.number_input("price", min_value=0.0, max_value=10000.0, value=17.45, step=0.01)
shopping_mall = st.text_input("shopping_mall", "Mall of America")
city = st.text_input("city", "Bloomington")
province_state = st.text_input("province_state", "Minnesota")
country = st.text_input("country", "US")
gender = st.text_input("gender", "Female")
age = st.number_input("age", min_value=18, max_value=100, value=25)
days_since_last_purchase = st.number_input("days_since_last_purchase", min_value=0, max_value=5000, value=1056)
tenure = st.number_input("tenure", min_value=0, max_value=50, value=8)
discount_used = st.number_input("discount_used", min_value=0, max_value=10, value=0)
purchase_frequency = st.number_input("purchase_frequency", min_value=0, max_value=100, value=30)
avg_purchase_value = st.number_input("avg_purchase_value", min_value=0.0, max_value=10000.0, value=280.82, step=0.01)
recency = st.number_input("recency", min_value=0, max_value=5000, value=1056)
purchase_per_tenure = st.number_input("purchase_per_tenure", min_value=0.0, max_value=100.0, value=3.75, step=0.01)
discount_ratio = st.number_input("discount_ratio", min_value=0.0, max_value=10.0, value=0.0, step=0.01)

if st.button("predict"):
    user_input = {
        "category": category,
        "item": item,
        "quantity": quantity,
        "price": price,
        "shopping_mall": shopping_mall,
        "city": city,
        "province_state": province_state,
        "country": country,
        "gender": gender,
        "age": age,
        "days_since_last_purchase": days_since_last_purchase,
        "tenure": tenure,
        "discount_used": discount_used,
        "purchase_frequency": purchase_frequency,
        "avg_purchase_value": avg_purchase_value,
        "recency": recency,
        "purchase_per_tenure": purchase_per_tenure,
        "discount_ratio": discount_ratio,
    }

    result = pred(user_input)
    if result == 1:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is not likely to churn.")
