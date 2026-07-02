# 🚗 Used Car Price Prediction Using Machine Learning

A Machine Learning web application that predicts the resale price of a used car based on its specifications using the XGBoost Regression algorithm.

---

# 📖 Overview

The **Used Car Price Prediction System** is a machine learning project that estimates the resale value of a used car using various vehicle specifications. The model analyzes important features such as brand, model, manufacturing year, mileage, engine capacity, fuel type, transmission, ownership history, insurance status, and kilometers driven to predict an estimated market price.

The project is deployed using **Streamlit**, allowing users to enter car details through a simple web interface and receive instant price predictions.

---

# 🎯 Problem Statement

Determining the fair market value of a used car can be challenging because many factors influence its price. Buyers often struggle to know whether a vehicle is fairly priced, while sellers may find it difficult to estimate an appropriate selling price.

This project aims to build a machine learning model that predicts the resale price of a used car based on historical data, helping users make informed buying and selling decisions.

---

# 📊 Dataset

The dataset contains information about used cars and their selling prices.

### Input Features

- Brand
- Model
- Manufacturing Year
- Mileage (km/l)
- Engine Capacity (CC)
- Fuel Type
- Transmission
- Owner Type
- Insurance Validity
- Kilometers Driven
- Number of Seats
- Car Age

### Target Feature

- Price

---

# 🛠️ Tools and Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Jupyter Notebook
- Git
- GitHub

---

# ⚙️ Methods

The project follows the complete Machine Learning pipeline:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Label Encoding
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Train-Test Split
- Model Training using XGBoost Regressor
- Model Evaluation
- Model Saving using Joblib
- Streamlit Deployment

---

# 📈 Key Insights

- Manufacturing year has a significant impact on resale price.
- Cars with lower kilometers driven generally have higher resale value.
- Premium brands tend to retain higher resale prices.
- Vehicle age is inversely related to selling price.
- Transmission type, ownership history, and insurance status also influence the predicted price.

---

# 💻 Dashboard / Model / Output

The Streamlit application allows users to:

- Select Brand
- Select Model
- Select Fuel Type
- Select Transmission
- Select Owner Type
- Select Insurance Status
- Enter Manufacturing Year
- Enter Mileage
- Enter Engine Capacity
- Enter Kilometers Driven
- Enter Number of Seats

After clicking the **Predict Price** button, the trained XGBoost model estimates the resale value of the selected used car.

---

# ▶️ How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/onavghire28/used-car-price-prediction.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd used-car-price-prediction
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 📊 Results & Conclusion

- **Algorithm Used:** XGBoost Regressor
- **Model Accuracy (R² Score):** **0.73**

The trained XGBoost model achieved an **R² score of 0.73**, indicating that it explains approximately **73% of the variation** in used car prices. The application successfully predicts estimated resale values based on vehicle specifications and demonstrates the practical application of machine learning in price prediction.

---

# 🚀 Future Work

The project can be further enhanced by:

- Increasing the dataset size
- Adding location-based pricing
- Including accident and service history
- Adding car condition information
- Comparing XGBoost with CatBoost and LightGBM
- Deploying the application on Streamlit Cloud
- Integrating real-time used car listings

---

# 📂 Project Structure

```
used-car-price-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── model_generation.ipynb
├── requirements.txt
├── README.md
├── dataset.csv
└── images/
```

---

## Project Report 
- [Project Report](https://github.com/onavghire28/Insurance-Charges-Prediction/blob/main/Report.pdf)

---

## Dashboard Image
- [Dashboard](https://github.com/onavghire28/Insurance-Charges-Prediction/blob/main/Dashboard_Image.png)


---


## Author
**Om A Navghire**  
Data Analytics Enthusiast | Machine Learning | Excel | SQL | Power BI | Python

📧 Email: navghireom@gmail.com

🔗 GitHub: https://github.com/onavghire28

🔗 LinkedIn: https://linkedin.com/in/your-linkedin-profile

---
## ⭐ If you found this project useful, please consider giving it a Star on GitHub!
---
