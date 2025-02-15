
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Vehicle One Year Resale Value Predictor")

# input widget for getting user values for X (feature matrix value)
price = st.slider("Price_in_thousands", min_value=0, max_value=100, value=20)
horsepower = st.slider("Horsepower", min_value=0, max_value=100, value=20)
eng_size = st.slider("Engine_size", min_value=0, max_value=100, value=20)

# After selesting price, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[price, horsepower, eng_size]])[0].round(2)
  st.write("The predicted one year resale value of your vehicle is", prediction, "thousand dollars")
