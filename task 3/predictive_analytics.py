import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 1. Load the dataset
data = pd.read_csv("sales_data.csv")

print("Original Data:")
print(data.head())

# 2. Convert Month into date format
data["Month"] = pd.to_datetime(data["Month"])

# 3. Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# 4. Remove missing values if any
data = data.dropna()

# 5. Create a numerical feature for time
data["Month_Number"] = range(1, len(data) + 1)

# 6. Separate input and output
X = data[["Month_Number"]]
y = data["Sales"]

# 7. Split data into training and testing data
train_size = int(len(data) * 0.8)

X_train = X[:train_size]
X_test = X[train_size:]

y_train = y[:train_size]
y_test = y[train_size:]

# 8. Create the Linear Regression model
model = LinearRegression()

# 9. Train the model
model.fit(X_train, y_train)

# 10. Predict sales for test data
y_pred = model.predict(X_test)

# 11. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("Root Mean Squared Error:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

# 12. Predict future sales for 2026
future_months = pd.DataFrame({
    "Month_Number": range(len(data) + 1, len(data) + 13)
})

future_predictions = model.predict(future_months)

future_dates = pd.date_range(
    start="2026-01-01",
    periods=12,
    freq="MS"
)

future_result = pd.DataFrame({
    "Month": future_dates,
    "Predicted_Sales": future_predictions
})

print("\nPredicted Sales for 2026:")
print(future_result)

# 13. Save predictions to a CSV file
future_result.to_csv("future_sales_predictions.csv", index=False)

# 14. Visualize actual sales and regression line
plt.figure(figsize=(10, 5))

plt.scatter(
    data["Month"],
    data["Sales"],
    label="Actual Sales"
)

plt.plot(
    data["Month"],
    model.predict(X),
    label="Regression Line"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Historical Sales and Regression Trend")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_regression.png")
plt.show()

# 15. Visualize future predictions
plt.figure(figsize=(10, 5))

plt.plot(
    future_result["Month"],
    future_result["Predicted_Sales"],
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Predicted Sales")
plt.title("Predicted Sales for 2026")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("future_sales_prediction.png")
plt.show()

print("\nProject completed successfully!")
print("Prediction file saved as future_sales_predictions.csv")
print("Graphs saved as sales_regression.png and future_sales_prediction.png")