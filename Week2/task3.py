# TASK 3:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)
marks = np.random.normal(loc=65, scale=12, size=500)
plt.hist(marks, bins=20, density=True, edgecolor="black")

x = np.linspace(min(marks), max(marks), 100)
y = norm.pdf(x, loc=65, scale=12)

plt.plot(x, y)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Density")

plt.show()
