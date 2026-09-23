# Customer Churn Prediction Using ML

This project predicts whether a customer is likely to churn based on e-commerce customer data. It combines data preprocessing, exploratory analysis, feature engineering, machine learning, and a Streamlit-based prediction interface.

The repository is built for learning and experimentation with real-world churn prediction workflows in Python.


## Overview

Customer churn prediction helps businesses identify customers who may stop buying in the future. This project uses historical transaction/customer information to train a machine learning model and predict churn risk.

The current repository includes:
- a churn analysis notebook with preprocessing and model training logic
- saved model artifacts for reuse
- a Streamlit app for user-driven churn prediction
- a dashboard app for data exploration
- a dataset for customer churn analysis


## Key Features

- Data cleaning and missing-value handling
- Feature engineering such as recency, purchase-per-tenure, and discount ratio
- Categorical encoding and numerical scaling
- Model training and evaluation using scikit-learn and XGBoost
- Streamlit deployment for user prediction input
- Data visualization using Matplotlib and Seaborn


## Tech Stack

- Python
- pandas
- numpy
- scikit-learn
- XGBoost
- matplotlib
- seaborn
- Streamlit

## Power BI Dashboards

This project includes Power BI dashboard visuals for customer churn analysis and customer segmentation. These dashboards help summarize churn trends, customer risk, and behavioral patterns in a business-friendly format.

### Dashboard highlights
- Churn risk overview across customers
- Customer segmentation by engagement and risk category
- Visual understanding of churn drivers and retention opportunities

### Dashboard images

![Power BI Dashboard](https://github.com/dataseekho/eccomerce-churn-analysis/blob/main/images/Customer%20Segmentation%20Dashboard%20-%20Power%20BI.png)

<img width="621" alt="customer_churn_analysis" src="https://github.com/user-attachments/assets/a6cb7b25-75c6-4bc5-b06d-8472f1616b6c" />

---

<img width="619" alt="customer_churn_analysis2" src="https://github.com/user-attachments/assets/62d068f8-1daf-44fe-87f7-da99c97a75c9" />

---

## Repository Structure

```text
Customer-Churn-Prediction-Using-ML/
├── dashboard/
│   └── ...
├── data/
│   └── fact_customer.csv
├── images/
│   └── ...
├── modelling/
│   ├── churn_analysis_pipeline.ipynb
│   ├── Fact_Customer_Table.ipynb
│   ├── churn_prediction_model.pkl
│   └── x_train.csv
├── streamlit_app/
│   ├── app.py
│   └── end_to_end_ml_model_app.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── venv/
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/najmarazzaq761/Customer-Churn-Prediction-Using-ML.git
cd Customer-Churn-Prediction-Using-ML
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


## Run the Project

### Run the churn prediction app

```bash
streamlit run streamlit_app/end_to_end_ml_model_app.py
```

### Run the dashboard app

```bash
streamlit run streamlit_app/app.py
```


## Model and Notebook Notes

- The preprocessing, feature engineering, and model experimentation are done in the notebook under `modelling/churn_analysis_pipeline.ipynb`.
- The trained model is saved as `modelling/churn_prediction_model.pkl`.
- The training features file is saved as `modelling/x_train.csv`.
- The end-to-end prediction app loads the trained model and applies preprocessing before predicting churn.


## Data

The dataset used in this project is stored in:

```text
data/fact_customer.csv
```

It contains customer-related features such as category, item, quantity, price, shopping mall, city, state, gender, age, tenure, purchase frequency, and churn label.


## Contribution

Contributions are welcome. You can:
- improve the preprocessing pipeline
- add new models or evaluation metrics
- clean up the dashboard UI
- improve documentation

Please create a feature branch, make your changes, and open a pull request.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Najma Razzaq


