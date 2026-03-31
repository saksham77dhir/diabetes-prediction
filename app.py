import streamlit as st
import pickle
import numpy as np

classifier = pickle.load(open('classifier.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Diabetes Prediction")

input_data = st.text_input("Enter 8 values separated by comma")

if st.button("Predict"):
    try:
        data = np.asarray(input_data.split(','), dtype=float)

        # reshape needed
        data = data.reshape(1, -1)
        
        data = scaler.transform(data)

        prediction = classifier.predict(data)

        if prediction[0] == 0:
            st.success("NON-diabetic")
        else:
            st.success("Diabetic")

    except Exception as e:
        st.error("Error: " + str(e))