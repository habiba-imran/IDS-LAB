import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read Test dataset
df = pd.read_csv("Week5/Test.csv")
# Display first 5 rows
print(df.head())
# 1. Line Plot
sns.lineplot(data=df, x="Outlet_Establishment_Year", y="Item_MRP")
plt.show()
# 2. Scatter Plot
sns.scatterplot(data=df, x="Item_MRP", y="Item_Visibility")
plt.show()
# 3. Displot
sns.displot(data=df, x="Item_MRP")
plt.show()
# 4. Histplot
sns.histplot(data=df, x="Item_Weight")
plt.show()
# 5. Joint Plot
sns.jointplot(data=df, x="Item_MRP", y="Item_Visibility")
plt.show()
# 6. Box Plot
sns.boxplot(x=df["Item_MRP"])
plt.show()