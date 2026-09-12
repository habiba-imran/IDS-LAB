from scipy import stats
import matplotlib.pyplot as plt

pass_count = 58
fail_count = 42

# Part (a): Binomial Hypothesis Test
result = stats.binomtest(pass_count, n=100,
                         p=0.5, alternative='greater')

p_value = result.pvalue

print("P-value:", p_value)

# Part (c): Histogram

outcomes = [1] * pass_count + [0] * fail_count

plt.hist(outcomes, bins=2, edgecolor='black')

plt.title("Pass and Fail Distribution")
plt.xlabel("Outcome (0 = Fail, 1 = Pass)")
plt.ylabel("Number of Students")

plt.show()
