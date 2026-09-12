import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class_X = [65, 70, 68, 74, 72, 80, 85, 60, 78, 69]
class_Y = [55, 60, 58, 62, 65, 70, 68, 72, 75, 59]

# Part (a): Class X

mean_X = np.mean(class_X)
median_X = np.median(class_X)
mode_X = stats.mode(class_X, keepdims=True)

variance_X = np.var(class_X, ddof=0)
std_X = np.sqrt(variance_X)

print("Class X")
print("Mean:", mean_X)
print("Median:", median_X)

if mode_X.count[0] == 1:
    print("Mode: No mode")
else:
    print("Mode:", mode_X.mode[0])

print(f"Variance: {variance_X:.2f}")
print(f"Standard Deviation: {std_X:.2f}")


# Class Y

mean_Y = np.mean(class_Y)
median_Y = np.median(class_Y)
mode_Y = stats.mode(class_Y, keepdims=True)

variance_Y = np.var(class_Y, ddof=0)
std_Y = np.sqrt(variance_Y)

print("\nClass Y")
print("Mean:", mean_Y)
print("Median:", median_Y)

if mode_Y.count[0] == 1:
    print("Mode: No mode")
else:
    print("Mode:", mode_Y.mode[0])

print(f"Variance: {variance_Y:.2f}")
print(f"Standard Deviation: {std_Y:.2f}")


# Part (b): Histogram of Class X

plt.hist(class_X, bins=5, edgecolor='black')
plt.title("Distribution of Class X Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()


# Histogram of Class Y

plt.hist(class_Y, bins=5, edgecolor='black')
plt.title("Distribution of Class Y Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()
