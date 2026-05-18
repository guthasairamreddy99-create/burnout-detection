import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Employee Burnout Risk Detection")

# Inputs
working_intensity = st.number_input("Working Hours", 1.0, 15.0, 8.0)
tasks = st.number_input("Task Count", 1.0, 30.0, 10.0)
breaks = st.number_input("Break Time", 0.0, 120.0, 30.0)
weekend = st.selectbox("Weekend Work", [0, 1])
emails_activity = st.number_input("Email Activity", 0.0, 500.0, 100.0)
sleep_hours = st.number_input("Sleep Hours", 1.0, 12.0, 7.0)

if st.button("Predict"):

    # Feature engineering
    workload_intensity = tasks / hours if hours != 0 else 0
    overwork_index = hours * (1 + weekend)
    recovery_ratio = break_time / hours if hours != 0 else 0
    productivity_pressure = emails / tasks if tasks != 0 else 0

    input_data = np.array([[working_hours, tasks, break_time, weekend, emails, sleep_hours,
                            workload_intensity, overwork_index,
                            recovery_ratio, productivity_pressure]])

    result = model.predict(input_data)

    labels = ["Low", "Medium", "High"]
    st.success(f"Burnout Risk: {labels[result[0]]}")
