# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:11:34 2021

@author: Bhargav
"""
# this used to practice git

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/MLProjects/Diabetes/diabetes.sav','rb'))

def diabetes_prediction(input_data):

    #changing the input data into numpy array
    input_data_np= np.asarray(input_data)

    #reshape the array as we are predicting for one
    input_reshaped = input_data_np.reshape(1,-1)

    prediction = loaded_model.predict(input_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'This Person Doesnt have Diabetes'
        
    else:
        return 'This Person Have Diabetes'

def main():
    #title for web page
    st.title('Diabetes Prediction')
    
    #getting the input data from the user
    #Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Enter Glucose Level')
    BloodPressure = st.text_input('Enter the BloodPressure')
    SkinThickness = st.text_input('Enter the SkinThickness')
    Insulin = st.text_input('Enter the Insulin value')
    BMI = st.text_input('Enter your Body Mass Index')
    DiabetesPedigreeFunction = st.text_input('Enter the DiabetesPedigreeFunction ')
    Age = st.text_input('Enter the Patient Age')
    
    
    
    #code for prediction
    diabetes = ''
    
    #creating button
    
    if st.button ('Click For Results'):
        diabetes = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

        
    st.success(diabetes)
    
    
    
if __name__ == '__main__':
    main()