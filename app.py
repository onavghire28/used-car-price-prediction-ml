import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🚗 Used Car Price Prediction")

st.write("Enter the details of your car")

# -------------------- INPUTS --------------------

brand = st.selectbox("Brand", [
    "Audi","BMW","Ford","Honda","Hyundai","Kia","Mahindra",
    "Mercedes","Nissan","Skoda","Tata","Toyota","Volkswagen"
])

models = {
    "Audi":["A4","Q3","Q5"],
    "BMW":["3 Series","X1","X3"],
    "Ford":["EcoSport","Endeavour","Figo"],
    "Honda":["Amaze","City","Civic"],
    "Hyundai":["Creta","Verna","i20"],
    "Kia":["Carens","Seltos","Sonet"],
    "Mahindra":["Bolero","Scorpio","XUV700"],
    "Mercedes":["C-Class","E-Class","GLA"],
    "Nissan":["Kicks","Magnite","Sunny"],
    "Skoda":["Kushaq","Octavia","Slavia"],
    "Tata":["Harrier","Nexon","Punch"],
    "Toyota":["Camry","Corolla","Yaris"],
    "Volkswagen":["Polo","Taigun","Virtus"]
}

model_name = st.selectbox("Model", models[brand])

fuel = st.selectbox("Fuel Type",
                    ["Petrol","Diesel","CNG","Electric","Hybrid"])

transmission = st.selectbox("Transmission",
                            ["Manual","Automatic"])

owner = st.selectbox(
    "Owner Type",
    ["First", "Second", "Third", "Fourth+"]
)

insurance = st.selectbox("Insurance Valid",
                         ["Yes","No"])

year = st.number_input("Manufacturing Year",2000,2026,2020)

mileage = st.number_input("Mileage (km/l)",5.0,40.0,18.0)

engine = st.number_input("Engine CC",800,5000,1500)

kms = st.number_input("Kilometers Driven",0,500000,50000)

seats = st.number_input("Seats",2,10,5)

# -------------------- PREDICTION --------------------

if st.button("Predict Price"):

    car_age = datetime.now().year - year

    columns = [
        'Year','Mileage_kmpl','Engine_CC','Transmission','Owner_Type',
        'Kms_Driven','Insurance_Valid','Seats','Car_Age',
        'Brand_Audi','Brand_BMW','Brand_Ford','Brand_Honda',
        'Brand_Hyundai','Brand_Kia','Brand_Mahindra',
        'Brand_Mercedes','Brand_Nissan','Brand_Skoda',
        'Brand_Tata','Brand_Toyota','Brand_Volkswagen',
        'Model_3 Series','Model_A4','Model_Amaze',
        'Model_Bolero','Model_C-Class','Model_Camry',
        'Model_Carens','Model_City','Model_Civic',
        'Model_Corolla','Model_Creta','Model_E-Class',
        'Model_EcoSport','Model_Endeavour','Model_Figo',
        'Model_GLA','Model_Harrier','Model_Kicks',
        'Model_Kushaq','Model_Magnite','Model_Nexon',
        'Model_Octavia','Model_Polo','Model_Punch',
        'Model_Q3','Model_Q5','Model_Scorpio',
        'Model_Seltos','Model_Slavia','Model_Sonet',
        'Model_Sunny','Model_Taigun','Model_Verna',
        'Model_Virtus','Model_X1','Model_X3',
        'Model_XUV700','Model_Yaris','Model_i20',
        'Fuel_Type_CNG','Fuel_Type_Diesel',
        'Fuel_Type_Electric','Fuel_Type_Hybrid',
        'Fuel_Type_Petrol'
    ]

    data = {col:0 for col in columns}

    # Numeric values
    data["Year"] = year
    data["Mileage_kmpl"] = mileage
    data["Engine_CC"] = engine
    data["Kms_Driven"] = kms
    data["Seats"] = seats
    data["Car_Age"] = car_age

    data["Transmission"] = 1 if transmission == "Manual" else 0

    owner_mapping = {
    "First": 0,
    "Second": 1,
    "Third": 2,
    "Fourth+": 3
}
    data["Owner_Type"] = owner_mapping[owner]

    data["Insurance_Valid"] = 1 if insurance == "Yes" else 0

    # One-Hot Encoding
    data[f"Brand_{brand}"] = 1
    data[f"Model_{model_name}"] = 1
    data[f"Fuel_Type_{fuel}"] = 1

    df = pd.DataFrame([data])

    # Scale only these columns
    scale_cols = [
        "Year","Mileage_kmpl","Engine_CC",
        "Owner_Type","Kms_Driven","Car_Age"
    ]

    df[scale_cols] = scaler.transform(df[scale_cols])

    prediction = model.predict(df)[0]

    st.success("Prediction Completed Successfully!")

    st.subheader("Estimated Car Price")

    st.metric(
    label="Predicted Price",
    value=f"₹ {prediction:,.2f}"
)

    st.write("---")

    st.write("### Car Details")
    st.write(f"**Brand:** {brand}")
    st.write(f"**Model:** {model_name}")
    st.write(f"**Fuel Type:** {fuel}")
    st.write(f"**Transmission:** {transmission}")
    st.write(f"**Owner:** {owner}")
    st.write(f"**Year:** {year}")

    