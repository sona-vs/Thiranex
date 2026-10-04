import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PART 1 - DATA CLEANING
# =========================

df = pd.read_csv("raw_sales_data_messy.csv")

df = df.drop_duplicates()

df["Region"] = df["Region"].str.strip().str.title()
df["Product"] = df["Product"].str.strip()
df["Category"] = df["Category"].str.strip().str.title()
df["Payment_Method"] = df["Payment_Method"].str.strip().str.upper()
df["Salesperson"] = df["Salesperson"].str.strip().str.title()

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    format="mixed",
    dayfirst=True
)

df.loc[df["Quantity"] < 0, "Quantity"] = 0
df.loc[df["Unit_Price"] < 0, "Unit_Price"] = 0

df["Customer_ID"] = df["Customer_ID"].fillna("Unknown")
df["Salesperson"] = df["Salesperson"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(5)
df["Unit_Price"] = df["Unit_Price"].fillna(1400)
df["Order_Date"] = df["Order_Date"].fillna(pd.Timestamp("2026-04-25"))

# =========================
# PART 2 - REPORTING
# =========================

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

category_sales = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
payment_sales = df.groupby("Payment_Method")["Revenue"].sum().sort_values(ascending=False)

print("\n========== SALES REPORT ==========")
print("\nTotal Revenue:", df["Revenue"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())

print("\nSales by Category:")
print(category_sales)

print("\nSales by Region:")
print(region_sales)

print("\nSales by Product:")
print(product_sales)

print("\nSales by Payment Method:")
print(payment_sales)

# =========================
# PART 3 - VISUALIZATION
# =========================

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 9))

# 1. Revenue by Category
plt.subplot(2, 2, 1)
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# 2. Revenue by Region
plt.subplot(2, 2, 2)
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

# 3. Revenue by Payment Method
plt.subplot(2, 2, 3)
payment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue by Payment Method")
plt.ylabel("")

# 4. Revenue by Product
plt.subplot(2, 2, 4)
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()

# Save all 4 charts as ONE image
plt.savefig("sales_charts.png", dpi=300)

plt.show()

print("\nAll 4 charts saved as sales_charts.png")

# =========================
# SAVE CLEANED DATA
# =========================

df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned data saved as cleaned_sales_data.csv")