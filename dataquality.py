import pandas as pd

df = pd.read_csv("superstore.csv")  # ← ADD THIS

print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

# 1. Missing values
print("\n🔴 Missing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 2. Duplicate rows
print(f"\n🔴 Duplicate Rows: {df.duplicated().sum()}")

# 3. Inconsistent formatting (check categories)
print("\n🔴 Unique Segments:", df['Segment'].unique())
print("🔴 Unique Regions:", df['Region'].unique())
print("🔴 Unique Categories:", df['Category'].unique())
print("🔴 Unique Ship Modes:", df['Ship Mode'].unique())

# 4. Outliers in Sales
print("\n🔴 Sales Outlier Check:")
print(df['Sales'].describe())
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Sales'] < Q1 - 1.5 * IQR) | (df['Sales'] > Q3 + 1.5 * IQR)]
print(f"Number of Sales outliers: {len(outliers)}")