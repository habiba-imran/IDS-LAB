import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
data = pd.read_csv("Week4/Train.csv")


# Display data
print("Data:")
print(data.head())


# Display datatypes
print("\nData Types:")
print(data.dtypes)


# Filter Frozen Foods
frozen = data[data["Item_Type"] == "Frozen Foods"]

print("\nFrozen Foods:")
print(frozen)


# Append 5 records
new_records = data.head(5)
data = pd.concat([data, new_records], ignore_index=True)

print("\nAfter Appending 5 Records:")
print(data.tail())


# Sort in ascending order
data = data.sort_values(by="Item_Identifier")

print("\nData in Ascending Order:")
print(data.head(10))


# ---------------------------------
# BEFORE HANDLING MISSING VALUES
# ---------------------------------

# Boxplot by Outlet_Type
data.boxplot(
    column="Item_Outlet_Sales",
    by="Outlet_Type"
)

plt.title("Boxplot Before")
plt.suptitle("")
plt.xlabel("Outlet Type")
plt.ylabel("Item Outlet Sales")
plt.xticks(rotation=20)
plt.show()


# Histogram by Outlet_Type
data.hist(
    column="Item_Outlet_Sales",
    by="Outlet_Type",
    bins=10
)

plt.suptitle("Histogram Before")
plt.show()

print("\nNumber of bins = 10")


# Check missing values
print("\nMissing Values Before:")
print(data.isnull().sum())


# Replace Item_Weight missing values with 1.00
data["Item_Weight"] = data["Item_Weight"].fillna(1.00)


# Replace Outlet_Size missing values with Small
data["Outlet_Size"] = data["Outlet_Size"].fillna("Small")

# Drop rows where Outlet_Type is missing
data = data.dropna(subset=["Outlet_Type"])

# Display number of rows after
print("\nNumber of Rows After:")
print(data.shape[0])


# Check missing values after
print("\nMissing Values After:")
print(data.isnull().sum())

# AFTER HANDLING MISSING VALUES

# Boxplot after
data.boxplot(
    column="Item_Outlet_Sales",
    by="Outlet_Type"
)

plt.title("Boxplot After")
plt.suptitle("")
plt.xlabel("Outlet Type")
plt.ylabel("Item Outlet Sales")
plt.xticks(rotation=20)
plt.show()
# Histogram after
data.hist(
    column="Item_Outlet_Sales",
    by="Outlet_Type",
    bins=10
)
plt.suptitle("Histogram After")
plt.show()
print("\nNumber of bins = 10")