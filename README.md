# 🏠 House Price Prediction using Machine Learning

An end-to-end machine learning project that predicts residential property prices using a real-world Kaggle dataset. The project demonstrates the complete machine learning lifecycle, including exploratory data analysis, preprocessing, feature engineering, model selection, hyperparameter tuning, evaluation, and deployment with Streamlit.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

Estimating house prices accurately is an important problem in the real estate industry. This project uses machine learning to predict property prices based on characteristics such as:

* Property size
* Number of rooms
* Construction year
* Property location
* Street type
* Furnishing status
* Property type
* Swimming pool availability

The final solution includes an interactive web application built with **Streamlit**, allowing users to estimate house prices by entering property information.

---

## 🎯 Objectives

* Explore and understand a real-world housing dataset.
* Clean and preprocess the data.
* Build and compare multiple regression models.
* Optimize model performance using GridSearchCV.
* Evaluate model performance using regression metrics.
* Deploy the final model as an interactive web application.

---

## 📊 Dataset

**Source:** Kaggle

The dataset contains **1,124 residential properties** with the following features:

| Feature       | Description                  |
| ------------- | ---------------------------- |
| Area_SqFt     | Property area in square feet |
| Rooms         | Number of rooms              |
| Build_Year    | Construction year            |
| Location      | Property location category   |
| Street_Type   | Road type                    |
| Furnishing    | Furnishing status            |
| Property_Type | House, Apartment or Villa    |
| Has_Pool      | Swimming pool availability   |
| Price         | Target variable              |

---

## 🧹 Data Preprocessing

The preprocessing pipeline includes:

* Missing value imputation
* Numerical feature scaling
* One-Hot Encoding for categorical variables
* Train/Test split
* Scikit-learn Pipelines
* ColumnTransformer

This ensures that all preprocessing steps are automatically applied during both training and prediction.

---

## 🤖 Machine Learning Models

Several regression algorithms were evaluated before selecting the final model.

Models explored include:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The final model was optimized using **GridSearchCV** to identify the best hyperparameters.

---

## 📈 Model Performance

The Random Forest Regressor achieved the best overall performance after hyperparameter tuning with GridSearchCV.

| Metric | Score |
|---------|-------|
| R² Score | **0.9096** |
| MAE | **$34147.15** |
| RMSE | **$43700.38** |

The model explains approximately **91%** of the variance in house prices while maintaining a relatively low prediction error. The results indicate that the Random Forest Regressor is capable of capturing the relationship between property characteristics and market value with high accuracy.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Streamlit
* Jupyter Notebook

---

## 📂 Project Structure

```text
house-price-prediction/

├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_hyperparameter_tuning.ipynb
│
├── src/
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/martinmorag/house-price-prediction.git
```

Navigate to the project folder:

```bash
cd house-price-prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit application:

```bash
streamlit run app/streamlit_app.py
```

---

## 📷 Application Preview

### House Price Prediction Dashboard

![Screenshot of Project](./images/project.png)

---

## 🌐 Live Demo

Try the deployed application here:

**https://house-price-prediction-tool-tbybkegrhkkte4qm2bqxbx.streamlit.app/**

---

## 📊 Exploratory Data Analysis

The exploratory analysis revealed several interesting relationships within the dataset.

| Price Distribution | Area vs Price |
|-------------------|---------------|
| ![](images/price_distribution.png) | ![](images/area_vs_price.png) |

| Correlation Heatmap | Feature Importance |
|----------------------|--------------------|
| ![](images/correlation_heatmap.png) | ![](images/feature_importance.png) |

---

## 📊 Prediction Performance

The scatter plot below compares the predicted house prices with the actual values in the test dataset.

A strong concentration of points around the diagonal line indicates good predictive performance.

![Prediction Performance](images/model_predictions.png)

---

## 💡 Key Insights

- Property area was the strongest predictor of house prices.
- Houses with more rooms generally had higher market values.
- Recently built properties tended to have higher selling prices.
- Random Forest significantly outperformed Linear Regression and Decision Tree models.
- Hyperparameter tuning improved overall predictive performance.

---

## 📚 Lessons Learned

Through this project I gained practical experience with:

- Exploratory Data Analysis (EDA)
- Feature engineering
- Regression modeling
- Hyperparameter tuning using GridSearchCV
- Building preprocessing pipelines with Scikit-learn
- Deploying machine learning models with Streamlit

---

## 🔮 Future Improvements

Possible future enhancements include:

* XGBoost and LightGBM implementation
* Advanced feature engineering
* Geographic coordinates
* Cross-validation improvements
* Model explainability with SHAP
* Docker containerization
* CI/CD pipeline
* Cloud deployment

---

## 👨‍💻 Author

**Martín Moraga**

Software Developer | Machine Learning Enthusiast

GitHub: https://github.com/martinmorag

LinkedIn: https://www.linkedin.com/in/martin-moraga-lopez-810077222/
<!-- 
Portfolio: https://yourportfolio.com -->
