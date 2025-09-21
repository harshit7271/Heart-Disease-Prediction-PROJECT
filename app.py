import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


st.title("Heart Disease Prediction by HARSHIT")
st.markdown("This app predicts whether a person has heart disease based on various health parameters provided by you as input.")

age = st.slider("Age", 10, 100, 20)
sex = st.selectbox("SEX", ['M', 'F'])
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'ta', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol Level", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ['Y', 'N'])
oldpeak = st.slider("Oldpeak(ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_'+sex: 1,
        'ChestPainType_'+chest_pain: 1,
        'RestingECG_'+resting_ecg: 1,
        'ExerciseAngina_'+exercise_angina: 1,
        'ST_Slope_'+st_slope: 1
    }
    input_df = pd.DataFrame([raw_input])


    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]
    
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
         st.error("The model predicts that you may have heart disease. Please consult a healthcare professional for a comprehensive evaluation.")
    else:
         st.success("The model predicts that you are unlikely to have heart disease. However, maintain a healthy lifestyle and regular check-ups.")
st.sidebar.header("App details :")
st.sidebar.info(
    "We created this machine learning model to predict if a person is prone to any heart disease based on the thier medical reports or not "
    "It is builtuilt with Streamlit & scikit-learn 💻"
)
name = st.sidebar.text_input("Enter patient name")
with st.sidebar.expander("Rate your experience of using our application"):
    rating = st.slider("Rate here", 1, 5, 3)
    st.write(f"HEY {name}, You rated our application {rating} out of 5")





