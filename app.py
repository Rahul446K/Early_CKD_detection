import numpy as np
import pandas as pd
import joblib 
import streamlit as st


# Load the model
ckd_model_bundle=joblib.load("ckd_model_bundle.joblib")
pipeline=ckd_model_bundle['pipeline']
features_names=ckd_model_bundle['features_names']

# Make Prediction Function

def ckd_prediction(user_input):
    user_input_df=pd.DataFrame([user_input],columns=features_names)
    
    # now make prediction
    
    prediction=pipeline.predict(user_input_df)
    
    if(prediction[0]==1):
        return "The person has CKD."
    else:
        return "The person has no CKD."
    
# Create input fields for the user

def main():
    # Title and Description fro the web app
    # st.title("Early Chronic Kidney Disease(CKD) Prediction Web App 🩺") 
    # st.header("Please enter the patient's data below:")

    st.markdown("<h1 style='text-align: center; color: #90e0ef;'>🩺 Early Chronic Kidney Disease (CKD) Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #adb5bd;'>A Machine Learning–Powered Health Assistant</h4>", unsafe_allow_html=True)
    st.markdown(
    "<h2 style='text-align: center; color: white;'>Please enter the patient's data below:</h2>",
    unsafe_allow_html=True
)
    # st.write("")  # for spacing
    # st.markdown("---")


    st.markdown("""
<div style="
    height:4px;
    background: linear-gradient(to right, #00b4d8, #48cae4, #90e0ef);
    border-radius: 10px;
    margin: 10px 0 25px 0;">
</div>
""", unsafe_allow_html=True)

    # st.markdown("<hr style='border: 1px solid #00C0F0;'>", unsafe_allow_html=True)



    # split layout
    col1, col2, col3,col4 = st.columns(4)
    
    
    with col1:
        age = st.number_input("Age (years)", min_value=0, value=48)
        bp = st.number_input("Blood Pressure (mm/Hg)", min_value=0, value=70)
        sg = st.selectbox("Specific Gravity", ["1.005", "1.010", "1.015", "1.020", "1.025"], index=0)
        al = st.selectbox("Albumin", [0, 1, 2, 3, 4, 5], index=4)
        su = st.selectbox("Sugar", [0, 1, 2, 3, 4, 5], index=0)
        rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"], index=0)
       


    with col2:
        pc = st.selectbox("Pus Cell", ["normal", "abnormal"], index=1)
        pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"], index=0)
        ba = st.selectbox("Bacteria", ["present", "notpresent"], index=1)
        bgr = st.number_input("Blood Glucose Random (mg/dl)", min_value=0.0, value=117.0, format="%.1f")
        bu = st.number_input("Blood Urea (mg/dl)", min_value=0.0, value=56.0, format="%.1f")
        sc = st.number_input("Serum Creatinine (mg/dl)", min_value=0.0, value=3.8, format="%.1f")
       
       
    with col3:
        sod = st.number_input("Sodium (mEq/L)", min_value=0.0, value=111.0, format="%.1f")
        pot = st.number_input("Potassium (mEq/L)", min_value=0.0, value=2.5, format="%.1f")
        hemo = st.number_input("Hemoglobin (gms)", min_value=0.0, value=11.2, format="%.1f")
        pcv = st.number_input("Packed Cell Volume", min_value=0.0, value=32.0, format="%.0f")
        wc = st.number_input("White Blood Cell Count (cells/cumm)", min_value=0, value=6700)
        rc = st.number_input("Red Blood Cell Count (millions/cmm)", min_value=0.0, value=3.9, format="%.1f")
       
    with col4:
        htn = st.selectbox("Hypertension", ["yes", "no"], index=0)
        dm = st.selectbox("Diabetes Mellitus", ["yes", "no"], index=1)
        cad = st.selectbox("Coronary Artery Disease", ["yes", "no"], index=1)
        appet = st.selectbox("Appetite", ["good", "poor"], index=1)
        pe = st.selectbox("Pedal Edema", ["yes", "no"], index=0)
        ane = st.selectbox("Anemia", ["yes", "no"], index=0)
        
        
    # code for prediction
    diagnosis=""

    # create a button for prediction
    if(st.button("🔍 Predict CKD Result")):
        
        # Gather User_input data
        user_input=[
                age, bp, sg, al, su, rbc, pc, pcc, ba,
                bgr, bu, sc, sod, pot, hemo, pcv, wc, rc,
                htn, dm, cad, appet, pe, ane
        ]

        # call the ckd_prediction function
        diagnosis=ckd_prediction(user_input)

        # display the result to the user
        # st.success(diagnosis)

        if "has CKD" in diagnosis:
            st.error("🚨 **The person has Chronic Kidney Disease (CKD).**")
        else:
            st.success("✅ **The person does not have Chronic Kidney Disease (CKD).**")


# call the main function to execute
if __name__=="__main__":
    main()
    


    
