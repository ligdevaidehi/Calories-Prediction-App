import pickle

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Set page title and layout
st.title("Calories Burned Calculator App")
# Add an image for visual appeal
st.image("img.jpeg", caption="Stay Fit and Healthy",width=700)
st.markdown("---")

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

# Sidebar column
with col1:
    st.sidebar.header("User Inputs")
    gender = st.selectbox("Select Gender", ("Male", "Female"))
    age = st.number_input("Enter Age", min_value=1, max_value=150, step=1)
    height = st.number_input("Enter Height (cm)", min_value=1, max_value=300, step=1)
    weight = st.number_input("Enter Weight (kg)", min_value=1, max_value=500, step=1)
    duration = st.number_input("Enter Workout Duration (minutes)", min_value=1, max_value=1440, step=1)
    heart_rate = st.number_input("Enter Heart Rate (bpm)", min_value=1, max_value=250, step=1)
    body_temp = st.number_input("Enter Body Temperature (°C)", min_value=30.0, max_value=43.0, step=0.1)
    predict_button = st.button("Predict Calories")

# Main content column
with col2:
    st.markdown("## Predicted Calories Burned")

    if predict_button:
        if gender == "Male":
            g = 0
        else:
            g = 1

        # Predict calories burned
        prediction = model.predict(pd.DataFrame(columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'],
                                                data=np.array([g, age, height, weight, duration, heart_rate, body_temp]).reshape(1, 7)))

        # Display result with a dynamic bar chart using Plotly Express
        chart_data = pd.DataFrame({"Type": ["Predicted Calories Burned"], "Calories": [prediction[0]]})
        fig = px.bar(chart_data, x="Type", y="Calories", text="Calories",
                     title="Calories Burned", labels={"x": "", "y": "Calories"},
                     color_discrete_sequence=px.colors.diverging.RdYlBu_r) # Change this hex color code
        fig.update_traces(texttemplate="%{text:.2f} calories", textposition="outside")
        st.plotly_chart(fig)


