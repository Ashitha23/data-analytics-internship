import pandas as pd

# Load both files
df_old = pd.read_csv("superstore.csv")
df_new = pd.read_csv("superstore_cleaned.csv")

print("=" * 50)
print("BEFORE vs AFTER COMPARISON")
print("=" * 50)

# 1. Shape
print("\n📊 Shape:")
print(f"  Before: {df_old.shape}")
print(f"  After:  {df_new.shape}")

# 2. Columns added
new_cols = set(df_new.columns) - set(df_old.columns)
print(f"\n🆕 New Columns Added: {new_cols}")

# 3. Date type check
print("\n📅 Date Column Types:")
print(f"  Before - Order Date: {df_old['Order Date'].dtype}")
print(f"  After  - Order Date: {df_new['Order Date'].dtype}")

# 4. Postal Code check
print("\n📮 Postal Code:")
print(f"  Before dtype : {df_old['Postal Code'].dtype}")
print(f"  After dtype  : {df_new['Postal Code'].dtype}")
print(f"  Before nulls : {df_old['Postal Code'].isnull().sum()}")
print(f"  After nulls  : {df_new['Postal Code'].isnull().sum()}")
print(f"  'Unknown' count after: {(df_new['Postal Code'] == 'Unknown').sum()}")

# 5. New columns sample
print("\n🔍 Sample of New Columns:")
print(df_new[['Order Date', 'Order Year', 'Order Month', 'Ship Date', 'Shipping Days']].head())

# 6. Duplicates
print(f"\n🗑️ Duplicates:")
print(f"  Before: {df_old.duplicated().sum()}")
print(f"  After:  {df_new.duplicated().sum()}")

print("\n✅ Comparison Complete!")