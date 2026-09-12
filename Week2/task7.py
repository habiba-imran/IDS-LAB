import numpy as np
import matplotlib.pyplot as plt
scores = [45, 48, 50, 52, 54, 55, 58, 60, 62, 65,
          68, 70, 72, 74, 76, 78, 80, 82, 85, 90]

# Part (a): Quartiles
q1 = np.percentile(scores, 25)
q2 = np.percentile(scores, 50)
q3 = np.percentile(scores, 75)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)

# Part (b): Percentiles
p10 = np.percentile(scores, 10)
p90 = np.percentile(scores, 90)

print("10th Percentile:", p10)
print("90th Percentile:", p90)

# Part (c): Box Plot
plt.boxplot(scores, patch_artist=True)
plt.title("Student Exam Scores")
plt.ylabel("Scores")
plt.show()
