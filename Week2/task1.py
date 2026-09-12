# TASK 1:
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
data = [5, 7, 8, 6, 5, 9, 10, 12, 15, 18, 20, 22, 25, 30, 35, 40, 42, 45, 50, 60]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0], "Count:", mode.count[0])

plt.hist(data, bins = 10, edgecolor="black")
plt.title("Distribution of Data")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.show()
