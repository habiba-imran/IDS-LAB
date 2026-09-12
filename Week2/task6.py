import numpy as np
from scipy import stats
responses = {"Product_A": 60, "Product_B": 40}
result = stats.binomtest(responses["Product_A"], n=100,
                         p=0.5, alternative='greater')
p_value = result.pvalue
print("P-value:", p_value)
p_hat = responses["Product_A"] / 100
standard_error = np.sqrt((p_hat * (1 - p_hat)) / 100)
lower = p_hat - 1.96 * standard_error
upper = p_hat + 1.96 * standard_error
print(f"95% Confidence Interval: ({lower:.3f}, {upper:.3f})")
