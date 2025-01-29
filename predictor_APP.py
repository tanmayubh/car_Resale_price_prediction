import streamlit as st
import joblib
import numpy as np
import os
import pandas as pd

# model_path = os.path.join(os.path.dirname(__file__), 'cars_resale_model')
# model = joblib.load(model_path)

import streamlit as st
import joblib  # Ensure you have joblib for loading models
import numpy as np

def main():
    # Title of the Streamlit app
    s1 = st.selectbox('Car Name', ("Maruti S PRESSO", "Hyundai Xcent", "Maruti Vitara Brezza", "Tata Tiago",
    "Maruti Swift", "Renault Kwid", "Hyundai Grand i10", "Maruti IGNIS",
    "Honda Brio", "Hyundai Elite i20", "Maruti Baleno", "Honda WR-V",
    "Honda Amaze", "Maruti Alto 800", "Maruti Celerio", "Ford Ecosport",
    "Maruti Ciaz", "Honda City", "Datsun Redi Go", "Hyundai Santro Xing",
    "Ford FREESTYLE", "Maruti Dzire", "Maruti Alto", "Hyundai NEW SANTRO",
    "Maruti Alto K10", "Maruti Swift Dzire", "Maruti Wagon R 1.0",
    "Hyundai GRAND I10 NIOS", "Maruti Celerio X", "Mahindra XUV500",
    "Hyundai Verna", "Hyundai VENUE", "Tata NEXON", "Mahindra KUV 100 NXT",
    "Toyota YARIS", "Mahindra XUV 3OO", "Renault TRIBER", "Mahindra TUV300",
    "Toyota Glanza", "Renault Duster", "Hyundai i10", "Nissan MAGNITE",
    "KIA SONET", "Maruti Ertiga", "Honda Jazz", "KIA SELTOS",
    "Volkswagen Ameo", "Renault Kiger", "Hyundai NEW I20", "Tata ALTROZ",
    "Maruti Ritz", "Nissan Micra", "Hyundai i20", "Hyundai Eon",
    "Hyundai Creta", "Toyota Etios Liva", "Maruti New Wagon-R",
    "Nissan Micra Active", "Tata PUNCH", "Volkswagen Polo", "Toyota Corolla Altis",
    "Honda Civic", "Volkswagen Vento", "Maruti S Cross", "Hyundai i20 Active",
    "Hyundai AURA", "Tata TIGOR", "Mahindra Thar", "Maruti XL6",
    "Skoda Rapid", "Datsun Go", "Toyota Etios", "Mahindra Kuv100",
    "Skoda SLAVIA", "Hyundai New Elantra", "Datsun Go Plus"))

    if s1 == "Maruti S PRESSO":
        p1 = 0
    elif s1 == "Hyundai Xcent":
        p1 = 1
    elif s1 == "Maruti Vitara Brezza":
        p1 = 2
    elif s1 == "Tata Tiago":
        p1 = 3
    elif s1 == "Maruti Swift":
        p1 = 4
    elif s1 == "Renault Kwid":
        p1 = 5
    elif s1 == "Hyundai Grand i10":
        p1 = 6
    elif s1 == "Maruti IGNIS":
        p1 = 7
    elif s1 == "Honda Brio":
        p1 = 8
    elif s1 == "Hyundai Elite i20":
        p1 = 9
    elif s1 == "Maruti Baleno":
        p1 = 10
    elif s1 == "Honda WR-V":
        p1 = 11
    elif s1 == "Honda Amaze":
        p1 = 12
    elif s1 == "Maruti Alto 800":
        p1 = 13
    elif s1 == "Maruti Celerio":
        p1 = 14
    elif s1 == "Ford Ecosport":
        p1 = 15
    elif s1 == "Maruti Ciaz":
        p1 = 16
    elif s1 == "Honda City":
        p1 = 17
    elif s1 == "Datsun Redi Go":
        p1 = 18
    elif s1 == "Hyundai Santro Xing":
        p1 = 19
    elif s1 == "Ford FREESTYLE":
        p1 = 20
    elif s1 == "Maruti Dzire":
        p1 = 21
    elif s1 == "Maruti Alto":
        p1 = 22
    elif s1 == "Hyundai NEW SANTRO":
        p1 = 23
    elif s1 == "Maruti Alto K10":
        p1 = 24
    elif s1 == "Maruti Swift Dzire":
        p1 = 25
    elif s1 == "Maruti Wagon R 1.0":
        p1 = 26
    elif s1 == "Hyundai GRAND I10 NIOS":
        p1 = 27
    elif s1 == "Maruti Celerio X":
        p1 = 28
    elif s1 == "Mahindra XUV500":
        p1 = 29
    elif s1 == "Hyundai Verna":
        p1 = 30
    elif s1 == "Hyundai VENUE":
        p1 = 31
    elif s1 == "Tata NEXON":
        p1 = 32
    elif s1 == "Mahindra KUV 100 NXT":
        p1 = 33
    elif s1 == "Toyota YARIS":
        p1 = 34
    elif s1 == "Mahindra XUV 3OO":
        p1 = 35
    elif s1 == "Renault TRIBER":
        p1 = 36
    elif s1 == "Mahindra TUV300":
        p1 = 37
    elif s1 == "Toyota Glanza":
        p1 = 38
    elif s1 == "Renault Duster":
        p1 = 39
    elif s1 == "Hyundai i10":
        p1 = 40
    elif s1 == "Nissan MAGNITE":
        p1 = 41
    elif s1 == "KIA SONET":
        p1 = 42
    elif s1 == "Maruti Ertiga":
        p1 = 43
    elif s1 == "Honda Jazz":
        p1 = 44
    elif s1 == "KIA SELTOS":
        p1 = 45
    elif s1 == "Volkswagen Ameo":
        p1 = 46
    elif s1 == "Renault Kiger":
        p1 = 47
    elif s1 == "Hyundai NEW I20":
        p1 = 48
    elif s1 == "Tata ALTROZ":
        p1 = 49
    elif s1 == "Maruti Ritz":
        p1 = 50
    elif s1 == "Nissan Micra":
        p1 = 51
    elif s1 == "Hyundai i20":
        p1 = 52
    elif s1 == "Hyundai Eon":
        p1 = 53
    elif s1 == "Hyundai Creta":
        p1 = 54
    elif s1 == "Toyota Etios Liva":
        p1 = 55
    elif s1 == "Maruti New Wagon-R":
        p1 = 56
    elif s1 == "Nissan Micra Active":
        p1 = 57
    elif s1 == "Tata PUNCH":
        p1 = 58
    elif s1 == "Volkswagen Polo":
        p1 = 59
    elif s1 == "Toyota Corolla Altis":
        p1 = 60
    elif s1 == "Honda Civic":
        p1 = 61
    elif s1 == "Volkswagen Vento":
        p1 = 62
    elif s1 == "Maruti S Cross":
        p1 = 63
    elif s1 == "Hyundai i20 Active":
        p1 = 64
    elif s1 == "Hyundai AURA":
        p1 = 65
    elif s1 == "Tata TIGOR":
        p1 = 66
    elif s1 == "Mahindra Thar":
        p1 = 67
    elif s1 == "Maruti XL6":
        p1 = 68
    elif s1 == "Skoda Rapid":
        p1 = 69
    elif s1 == "Datsun Go":
        p1 = 70
    elif s1 == "Toyota Etios":
        p1 = 71
    elif s1 == "Mahindra Kuv100":
        p1 = 72
    elif s1 == "Skoda SLAVIA":
        p1 = 73
    elif s1 == "Hyundai New Elantra":
        p1 = 74
    elif s1 == "Datsun Go Plus":
        p1 = 75


    p2 = st.number_input("Duration since purchase new")
    p3 = st.number_input("Distance travelled in KMs")
    p4 = st.number_input("Number of last owners")

    s5 = st.selectbox("Fuel type", ("PETROL", "DIESEL", "CNG")
    if s5 == "PETROL":
          p5 = 0
      elif s5 == "DIESEL":
          p5 = 1
    elif s5 == "CNG":
          p5 = 2


    s6 = st.selectbox("Location", ("HR", "TN", "WB", "MH", "UP", "KA", 
                               "PB", "GJ", "DL", "CH", "TS", "KL", 
                               "RJ", "AP", "MP", "BR"))

    if s6 == "HR":
      p6 = 0
    elif s6 == "TN":
      p6 = 1
    elif s6 == "WB":
      p6 = 2
    elif s6 == "MH":
      p6 = 3
    elif s6 == "UP":
      p6 = 4
    elif s6 == "KA":
      p6 = 5
    elif s6 == "PB":
      p6 = 6
    elif s6 == "GJ":
      p6 = 7
    elif s6 == "DL":
      p6 = 8
    elif s6 == "CH":
      p6 = 9
    elif s6 == "TS":
      p6 = 10
    elif s6 == "KL":
      p6 = 11
    elif s6 == "RJ":
      p6 = 12
    elif s6 == "AP":
      p6 = 13
    elif s6 == "MP":
      p6 = 14
    elif s6 == "BR":
      p6 = 15

    s7 = st.selectbox("Drive", ("Manual", "Automatic"))
    if s7 == "Manual":
      p7 = 0
    elif s7 == "Automatic":
      p7 = 1

    s8 = st.selectbox("Type", ("HatchBack", "Sedan", "SUV", "Lux_SUV", "Lux_sedan"))
    if s8 == "HatchBack":
      p8 = 0
    elif s8 == "Sedan":
      p8 = 1
    elif s8 == "SUV":
      p8 = 2
    elif s8 == "Lux_SUV":
      p8 = 3
    elif s8 == "Lux_sedan":
      p8 = 4


    print(f"Inputs: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}, {p7}, {p8}")
    input_data = np.array([[p1, p2, p3, p4, p5, p6, p7, p8]])
    print(f"Input data shape: {input_data.shape}")

    # Predict button
    if st.button("Predict"):
        try:
            prediction = predictive_model.predict(input_data)
            st.balloons() 
            st.success(f"Best resale price of your car {round(prediction[0], 2)} INR")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == '__main__':
    main()

