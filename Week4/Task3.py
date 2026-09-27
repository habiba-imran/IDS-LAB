# The data set is given Train dataset, you have to solve the null or missing values by 
# all the best possible ways. Handle the null values for the particular columns also. 


import pandas as pd

df = pd.read_csv('Week4/Train.csv')

print(df.isnull().sum())

# 1. Fill all null values with 0
df1 = df.fillna(value=0)
print(df1)


# 2. Fill all null values with 2
df2 = df.fillna(value=2)
print(df2)


# 3. Forward fill (previous value)
df3 = df.fillna(method='pad')
print(df3)


# 4. Backward fill (next value)
df4 = df.fillna(method='bfill')
print(df4)


# 5. Forward fill along columns
df5 = df.fillna(method='pad', axis=1)
print(df5)


# 6. Backward fill along columns
df6 = df.fillna(method='bfill', axis=1)
print(df6)


# 7. Fill null values of a particular column
df7 = df.copy()
df7['Outlet_Size'] = df7['Outlet_Size'].fillna('Medium')
print(df7[['Outlet_Size']])


# 8. Fill numerical column with mean
df8 = df.copy()
df8['Item_Weight'] = df8['Item_Weight'].fillna(df8['Item_Weight'].mean())
print(df8[['Item_Weight']])


# 9. Fill numerical column with minimum
df9 = df.copy()
df9['Item_Weight'] = df9['Item_Weight'].fillna(df9['Item_Weight'].min())
print(df9[['Item_Weight']])


# 10. Fill numerical column with maximum
df10 = df.copy()
df10['Item_Weight'] = df10['Item_Weight'].fillna(df10['Item_Weight'].max())
print(df10[['Item_Weight']])


# 11. Drop rows containing null values
df11 = df.dropna()
print(df11)


# 12. Drop rows if ANY value is null
df12 = df.dropna(how='any')
print(df12)


# 13. Drop rows only if ALL values are null
df13 = df.dropna(how='all')
print(df13)


# Check total number of null values
print(df.isnull().sum().sum())