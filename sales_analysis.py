# Supermarket Sales Data Processing & Visualization
# Author: Nithishkumar K
# GitHub: https://github.com/nithish9208

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# ----- Data Cleaning -----
# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# ----- Analysis -----
# Total sales by branch
branch_sales = df.groupby("branch")["total"].sum()
print("\nTotal Sales by Branch:\n", branch_sales)

# Monthly sales trend
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["total"].sum()

# Average spending by gender
gender_spending = df.groupby("gender")["total"].mean()

# ----- Visualization -----
plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title("Total Sales by Branch")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=gender_spending.index, y=gender_spending.values)
plt.title("Average Spending by Gender")
plt.ylabel("Average Sales")
plt.show()
