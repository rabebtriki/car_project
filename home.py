import streamlit as st
from PIL import Image

def home_page():
    st.title("Welcome to Car Selection and Analysis Platform")
    
    st.write("### About This Application")
    st.write(
        "This platform consists of three main components: **Car Selection and Filtering**, **Interactive Car Chat**, "
        "and **Car Price Prediction**. It is designed to help users find, interact with, and predict the value of cars."
    )
    
    st.write("### How It Works")
    st.write(
        "1. **Car Selection and Filtering**: Choose a car based on filters such as brand, model, and features to find the best option for your needs.\n"
        "2. **Interactive Car Chat**: After selecting a car, you can chat with a virtual car expert or the car itself to get answers to any questions.\n"
        "3. **Car Price Prediction**: Get a price prediction for a chosen car based on its characteristics, such as model, year, and mileage."
    )
    
    st.write("### Technology Behind the Application")
    st.write("Our platform uses advanced AI models and predictive algorithms to offer a unique and interactive experience, ensuring accurate results and helpful insights.")