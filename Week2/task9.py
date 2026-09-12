import numpy as np
import matplotlib.pyplot as plt

ad_spend = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sales = [25, 28, 35, 40, 45, 50, 60, 68, 75, 85]
# Part (a): Scatter Plot
plt.scatter(ad_spend, sales)
plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend ($1000)")
plt.ylabel("Sales ($1000)")
plt.show()
# Part (b): Correlation
correlation = np.corrcoef(ad_spend, sales)[0, 1]
print(f"Correlation Coefficient: {correlation:.2f}")
