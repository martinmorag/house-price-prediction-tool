import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import joblib
import pandas as pd
import streamlit as st

import src.config as config

print("Config file:", config.__file__)
print("MODEL_PATH:", config.MODEL_PATH)

MODEL_PATH = config.MODEL_PATH

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction")

st.markdown("""
Estimate the market value of a residential property using a machine learning model trained on historical housing data.

Enter the property characteristics in the sidebar and click **Predict Price**.
""")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.sidebar.header("Property Details")

area = st.sidebar.number_input(
    "Area (Sq Ft)",
    min_value=500,
    max_value=15000,
    value=2200
)

rooms = st.sidebar.slider(
    "Rooms",
    2,
    10,
    4
)

build_year = st.sidebar.slider(
    "Build Year",
    1980,
    2025,
    2015
)

location = st.sidebar.selectbox(
    "Location",
    [
        "Urban",
        "Suburban",
        "Rural"
    ]
)

street = st.sidebar.selectbox(
    "Street Type",
    [
        "Paved",
        "Gravel"
    ]
)

furnishing = st.sidebar.selectbox(
    "Furnishing",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)

property_type = st.sidebar.selectbox(
    "Property Type",
    [
        "House",
        "Apartment",
        "Villa"
    ]
)

pool = st.sidebar.selectbox(
    "Swimming Pool",
    [
        "Yes",
        "No"
    ]
)

input_data = pd.DataFrame({

    "Area_SqFt": [area],
    "Rooms": [rooms],
    "Build_Year": [build_year],
    "Location": [location],
    "Street_Type": [street],
    "Furnishing": [furnishing],
    "Property_Type": [property_type],
    "Has_Pool": [pool]

})

predict_button = st.button("Predict Price")

if predict_button:

    prediction = model.predict(input_data)[0]

    st.success("Prediction completed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Estimated Price",
            f"${prediction:,.2f}"
        )

    with col2:
        st.metric(
            "Property Size",
            f"{area:,.0f} sq ft"
        )

    st.subheader("Property Summary")
    st.dataframe(input_data, use_container_width=True)

with st.expander("About the Machine Learning Model"):

    st.markdown("""

This application uses a **Random Forest Regressor** trained on historical housing data.

The prediction pipeline includes:

- Missing value imputation
- Feature scaling
- One-Hot Encoding
- Hyperparameter tuning using GridSearchCV

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The prediction should be interpreted as an estimate rather than an exact market valuation.

""")
    
st.markdown("---")

st.caption(
    "Developed by Martín Moraga • Machine Learning Portfolio Project"
)