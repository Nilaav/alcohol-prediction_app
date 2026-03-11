import streamlit as st
import pickle
import numpy as np

# Load model safely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# App title
st.title("Alcohol Consumption Predictor")

st.write("Enter the values to predict total litres of pure alcohol consumption.")

# User inputs
beer = st.number_input("Beer Servings", min_value=0.0)
spirit = st.number_input("Spirit Servings", min_value=0.0)
wine = st.number_input("Wine Servings", min_value=0.0)

continent = st.selectbox(
    "Select Continent",
    ["Asia", "Europe", "Africa", "North America", "South America", "Oceania"]
)

# Convert continent into dummy variables
continent_Asia = 1 if continent == "Asia" else 0
continent_Europe = 1 if continent == "Europe" else 0
continent_North_America = 1 if continent == "North America" else 0
continent_Oceania = 1 if continent == "Oceania" else 0
continent_South_America = 1 if continent == "South America" else 0

# Feature array
features = np.array([[beer, spirit, wine,
                      continent_Asia,
                      continent_Europe,
                      continent_North_America,
                      continent_Oceania,
                      continent_South_America]])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(features)
    st.success(f"Predicted Alcohol Consumption: {prediction[0]:.2f} litres")