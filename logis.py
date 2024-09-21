import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pickle
import time


pickle_in = open('heart-disease-prediction.pkl', 'rb') 
classifier = pickle.load(pickle_in)


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

def welcome():
    return 'welcome all'

def pridiction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

    prediiction=classifier.predict(
        [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    )
    print(prediiction)
    return prediiction


def main():
    st.title("heart disease pridiction")


    html_temp="""
    <div style ="background-colour:red;padding:15px"> 
    <h1 style ="color:white;text-align:center;">disease pridiction Classifier ML App </h1> 
    </div> """


    st.markdown(html_temp,unsafe_allow_html=True)

    
age = st.text_input("age","")
sex = st.text_input("gender","")
cp = st.text_input("chest pain","")
trestbps = st.text_input("Resting Blood pressure","")
chol= st.text_input("cholestrol","")
fbs= st.text_input("Fasting Blood  Suger","")
restecg= st.text_input("Resting Electrocardiographic Result","")
thalach = st.text_input("Maximum Heart Rate Archived","")
exang = st.text_input("Exercise Incduced Angina","")
oldpeak= st.text_input("ST Depression Induced by Exercise Relative to Rest","")
slope= st.text_input("Slope of the peak exercise ST segment","")
ca = st.text_input("Number of magor vessels""")
thal= st.text_input("Thalassemia","")
result=""


if st.button("Predict"): 
        result = pridiction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal) 
        st.write(result)

        if pridiction == (1):
           print("go to the doctor")
        else:
          print("safe")

          

 
     




if __name__=='__main__': 
    main() 
    
    

    
