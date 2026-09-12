# TASK 2:
import numpy as np
import matplotlib.pyplot as plt	
dataset_A = [50, 52, 51, 49, 50, 51, 50, 49, 52, 50]  # low variance
dataset_B = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]  # high variance

variance_A = np.var(dataset_A, ddof=0)
std_dev_A = np.sqrt(variance_A)
range_A = np.max(dataset_A) - np.min(dataset_A)
print(f"Dataset A Variance: {variance_A:.2f}")
print(f"Dataset A Standard deviation: {std_dev_A:.2f}")
print(f"Dataset A Range: {range_A}")

variance_B = np.var(dataset_B, ddof=0)
std_dev_B = np.sqrt(variance_B)
range_B = np.max(dataset_B) - np.min(dataset_B)
print(f"Dataset B Variance: {variance_B:.2f}")
print(f"Dataset B Standard deviation: {std_dev_B:.2f}")
print(f"Dataset B Range: {range_B}")

data = [dataset_A, dataset_B]
plt.boxplot(data, tick_labels=['Dataset A', 'Dataset B'], patch_artist=True)
plt.show()
