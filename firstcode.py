import pandas as pd

df = pd.read_csv("superstore.csv")

# Create a data dictionary
data_dict = {
    'Column': df.columns.tolist(),
    'Data Type': df.dtypes.astype(str).tolist(),
    'Non-Null Count': df.notnull().sum().tolist(),
    'Null Count': df.isnull().sum().tolist(),
    'Unique Values': [df[col].nunique() for col in df.columns],
    'Sample Value': [df[col].iloc[0] for col in df.columns],
    'Business Meaning': [
        'Unique row identifier',
        'Unique order identifier',
        'Date when order was placed',
        'Date when order was shipped',
        'Shipping method chosen',
        'Unique customer identifier',
        'Full name of customer',
        'Customer segment (Consumer/Corporate/Home Office)',
        'Country of order',
        'City of order',
        'State of order',
        'Postal/ZIP code',
        'Sales region (East/West/Central/South)',
        'Unique product identifier',
        'Product category (Furniture/Office Supplies/Technology)',
        'Product sub-category',
        'Full product name',
        'Revenue from the order'
    ]
}

data_dictionary = pd.DataFrame(data_dict)
print(data_dictionary.to_string())

# Save it
data_dictionary.to_csv("data_dictionary.csv", index=False)
print("\n✅ Data dictionary saved!")