# Week 1 – Sales Analysis Dashboard

This dashboard was created as part of my Week 1 internship task at Geranx.

## Dashboard Overview

The Sales Analysis Dashboard provides an overview of sales performance using different visualizations and key metrics.

### Key Metrics
- Total Customers: 50
- Total Revenue: 111K
- Total Units: 25K
- Total Products: 21

### Visualizations
- Revenue by Category
- Revenue by Date
- Revenue by Region
- Quantity by Category

## Tools Used

- Power BI
- Data Visualization
- Data Analysis

## Power BI Report

The `.pbix` file is included in this repository and can be downloaded and opened using Power BI Desktop.


# Week 2 – Customer Segmentation

## Task
Customer Segmentation based on customer behavior and demographics.

## Work Done
- Loaded and analyzed the customer dataset.
- Preprocessed the data and performed feature scaling.
- Applied K-Means clustering to group similar customers.
- Analyzed the different customer segments.
- Saved the trained model and scaler.

## Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- VS Code

## Files
- `segmentation.py` – Python code for customer segmentation
- `customer_segmentation.xlsx` – Customer dataset
- `kmeans_model.pkl` – Trained K-Means model
- `scaler.pkl` – Saved scaler
- `Analysis_model.ipynb` – Analysis file

 # WEEK 3 Predictive Analytics Using Historical Data

## 📌 Project Overview

This project focuses on predicting future sales using historical sales data.

The historical data is cleaned and analyzed, and a Linear Regression model is used to predict future sales. The results are visualized using graphs to understand the sales trend and predicted values.

## 🎯 Objective

- Analyze historical sales data
- Clean and prepare the dataset
- Build a predictive model using Linear Regression
- Predict future sales
- Visualize actual and predicted sales

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Excel

## 📂 Files in This Project

- `sales_data.xlsx` – Historical sales dataset
- `future_sales_predictions.xlsx` – Predicted future sales
- `predictive_analytics.py` – Python code used for analysis and prediction
- `sales_regression.png` – Sales regression graph
- `future_sales_prediction.png` – Future sales prediction graph

## 🔄 Project Workflow

1. Load the historical sales dataset.
2. Clean and prepare the data.
3. Analyze the sales data.
4. Apply Linear Regression.
5. Predict future sales.
6. Visualize the results using graphs.
7. Save the predictions in an Excel file.

## 📊 Results

The Linear Regression model was used to identify the relationship between the historical data and sales values. The project generates graphs showing the sales trend and future sales predictions.

# Week 4 – Data Cleaning & Reporting Automation

## Overview

As part of Week 4 of my internship, I worked on a **Data Cleaning & Reporting Automation** task using Python.

The main objective was to clean a messy sales dataset, handle missing and invalid data, perform basic sales analysis, and create visual reports from the cleaned data.

---

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- CSV Dataset

---

## Task Objectives

- Load and inspect the raw sales dataset
- Remove duplicate records
- Handle missing values
- Fix invalid and negative values
- Standardize text data
- Convert date values into the correct format
- Calculate revenue
- Analyze sales by different categories
- Create visualizations
- Export the cleaned dataset

---

## Steps Performed

### 1. Load the Dataset

The raw sales dataset was loaded using Pandas.

```python
df = pd.read_csv("raw_sales_data_messy.csv")


