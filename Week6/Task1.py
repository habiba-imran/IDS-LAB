
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# Sample dataset
df = pd.DataFrame({
    "City": ["Islamabad", "Lahore", "Karachi", "Lahore", "Islamabad", "Karachi", "Lahore", "Islamabad"],
    "Size": ["Small", "Medium", "Large", "Small", "Large", "Medium", "Large", "Small"],
    "Purchased": ["No", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes"]
})

print("Original Dataset:")
print(df)

# 1. Dummy Variable Encoding
print("\n1. Dummy Variable Encoding")
print(pd.get_dummies(df["City"], prefix="City", drop_first=True, dtype=int))

# 2. One-Hot Encoding
print("\n2. One-Hot Encoding")
print(pd.get_dummies(df["City"], prefix="City", dtype=int))

# 3. Label Encoding
print("\n3. Label Encoding")
df["Purchased_Label"] = LabelEncoder().fit_transform(df["Purchased"])
print(df[["Purchased", "Purchased_Label"]])

# 4. Ordinal Encoding
print("\n4. Ordinal Encoding")
df["Size_Ordinal"] = OrdinalEncoder(
    categories=[["Small", "Medium", "Large"]]
).fit_transform(df[["Size"]]).astype(int)
print(df[["Size", "Size_Ordinal"]])

# 5. Frequency Encoding
print("\n5. Frequency Encoding")
df["City_Frequency"] = df["City"].map(df["City"].value_counts())
print(df[["City", "City_Frequency"]])

# 6. Binary Encoding
print("\n6. Binary Encoding")
codes = pd.Categorical(df["City"]).codes + 1
binary = pd.DataFrame(
    [list(format(x, "02b")) for x in codes],
    columns=["Bit1", "Bit2"]
).astype(int)
print(binary)

# 7. Mean Encoding
print("\n7. Mean Encoding")
df["City_Mean"] = df.groupby("City")["Purchased_Label"].transform("mean")
print(df[["City", "City_Mean"]])
