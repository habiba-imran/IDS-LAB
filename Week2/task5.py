import numpy as np
import matplotlib.pyplot as plt
dept_A = [40000, 42000, 45000, 46000, 47000, 48000, 49000, 52000, 53000, 54000]
dept_B = [30000, 32000, 35000, 36000, 37000, 42000, 45000, 46000, 47000, 50000]
dept_C = [25000, 26000, 27000, 28000, 29000, 50000, 52000, 55000, 60000, 65000]

data = [dept_A, dept_B, dept_C]
plt.boxplot(data, tick_labels=['Department A', 'Department B', 'Department C'],
            patch_artist=True)

plt.title("Monthly Salaries of Three Departments")
plt.ylabel("Salary")
plt.show()

q1_A = np.percentile(dept_A, 25)
q3_A = np.percentile(dept_A, 75)
iqr_A = q3_A - q1_A

q1_B = np.percentile(dept_B, 25)
q3_B = np.percentile(dept_B, 75)
iqr_B = q3_B - q1_B

q1_C = np.percentile(dept_C, 25)
q3_C = np.percentile(dept_C, 75)
iqr_C = q3_C - q1_C

print("IQR of Department A:", iqr_A)
print("IQR of Department B:", iqr_B)
print("IQR of Department C:", iqr_C)
