import pandas as pd
df = pd.read_csv("superstore.csv")

# 1. Convert date columns — dayfirst=True because format is DD/MM/YYYY
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
print("✅ Dates converted")

# 2. Fix Postal Code — treat as string, not float
df['Postal Code'] = df['Postal Code'].fillna(0).astype(int).astype(str)
df['Postal Code'] = df['Postal Code'].replace('0', 'Unknown')
print("✅ Postal Code fixed")

# 3. Drop duplicate rows if any
df.drop_duplicates(inplace=True)
print("✅ Duplicates removed")

# 4. Feature Engineering — new useful columns
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
print("✅ New columns added: Order Year, Order Month, Shipping Days")

# 5. Save cleaned dataset
df.to_csv("superstore_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as superstore_cleaned.csv")
print("Final Shape:", df.shape)