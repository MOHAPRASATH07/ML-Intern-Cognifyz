# 🍽️ Restaurant Rating Prediction using Machine Learning

## 📌 Project Overview

This project was developed as part of the **Machine Learning Internship at Cognifyz Technologies**.

The objective is to build a machine learning model capable of predicting restaurant ratings based on restaurant-related features such as customer votes, pricing, cost, and cuisine information.

This project demonstrates a complete end-to-end machine learning workflow including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, evaluation, and deployment.

---

## 🎯 Problem Statement

Restaurant ratings play an important role in customer decision-making and business growth.
The goal of this project is to predict the **Aggregate Rating** of a restaurant using machine learning techniques.

### Target Variable:

* Aggregate Rating

### Input Features:

* Votes
* Average Cost for Two
* Price Range
* Cuisine Count

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit

---

## 📂 Dataset Information

The dataset contains restaurant-related information such as:

* Restaurant Name
* City
* Cuisines
* Votes
* Average Cost for Two
* Price Range
* Aggregate Rating

The dataset was analyzed to understand patterns affecting restaurant ratings.

---

## 🧹 Data Preprocessing

Before model training, the dataset was cleaned and prepared.

### Steps Performed:

* Checked missing values
* Handled missing values in cuisine feature
* Removed duplicate records
* Fixed encoding issues
* Selected important features for model training

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to discover insights and patterns in the dataset.

### Analysis Performed:

* Missing value analysis
* Distribution of numerical features
* Correlation analysis
* Feature relationship with target variable
* Restaurant rating distribution
* Votes vs Rating analysis
* Price Range vs Rating analysis

### Key Insights:

* Restaurants with higher votes generally have better ratings
* Price range moderately impacts ratings
* Restaurants offering multiple cuisines often receive better ratings

---

## ⚙️ Feature Engineering

New features were created to improve model performance.

### Engineered Features:

* **Cuisine Count** → Number of cuisines offered
* **Expensive** → High-price restaurants indicator
* **Popular** → Restaurants with high customer engagement
* **Multiple Cuisines** → Binary indicator for multiple cuisines
* **Online Delivery** → Converted categorical feature into numerical form

These engineered features helped the model learn hidden patterns more effectively.

---

## 🤖 Model Building

Multiple machine learning models were trained and compared.

### Models Used:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The purpose of testing multiple models was to identify the best-performing algorithm.

---

## 📈 Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Model Performance

| Model             | MAE   | MSE   | R² Score |
| ----------------- | ----- | ----- | -------- |
| Linear Regression | 1.070 | 1.698 | 0.258    |
| Decision Tree     | -     | -     | 0.900    |
| Random Forest     | 0.240 | 0.136 | 0.940    |

---

## 🏆 Best Model

### Random Forest Regressor

Random Forest achieved the best performance.

### Performance:

* MAE = 0.240
* MSE = 0.136
* R² Score = 0.940

### Why Random Forest?

* Handles nonlinear relationships well
* Captures feature interactions effectively
* Reduces overfitting using ensemble learning

---

## 💡 Business Insights

Key factors influencing restaurant ratings:

* Customer votes strongly influence ratings
* Higher price range restaurants tend to have better ratings
* Restaurants serving multiple cuisines often perform better
* Customer engagement improves restaurant reputation

These insights can help restaurant businesses improve customer satisfaction and service quality.

---

## 🚀 Deployment

The trained model was deployed using **Streamlit** for real-time predictions.

Users can provide:

* Votes
* Average Cost for Two
* Price Range
* Cuisine Count

The application predicts restaurant ratings instantly.

Run locally using:

```bash
streamlit run app/app.py
```

---

## 📁 Project Structure

```bash
Restaurant-Rating-Prediction/
│
├── data/
├── notebook/
├── model/
├── app/
├── requirements.txt
├── README.md
```

---

## 🔮 Future Improvements

Possible improvements for this project:

* Use advanced models like XGBoost
* Add location-based features
* Improve feature engineering
* Deploy on cloud platforms
* Build a complete recommendation system

---

## ✅ Conclusion

This project successfully developed a machine learning model to predict restaurant ratings.

The project covered the complete machine learning pipeline:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Model Training
* Model Evaluation
* Deployment

Among all models tested, **Random Forest Regressor** delivered the best performance with an **R² score of 0.94**.

This project demonstrates practical machine learning implementation for solving real-world business problems.

---

## 👨‍💻 Author

Machine Learning Internship Project
Cognifyz Technologies

