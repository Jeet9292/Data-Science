import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
# One-Sample t-Test
sample_data = [2.7, 2.0, 2.8, 2.6, 2.0] # Sample resolution times
population_mean = 2 # Null hypothesis: mean = 2 days
t, p= ttest_1samp(sample_data, population_mean)
print("\n--- One-Sample t-Test ---")
print(f"T-statistic: {t:.2f}, P-value: {p:.4f}")
if p < 0.05:
 print("Reject H0")
else:
 print("Fail to reject H0")
sample1 = np.random.normal(loc=10, scale=2, size=15) # Class A scores
sample2 = np.random.normal(loc=12, scale=2, size=15) # Class B scores
t, p = ttest_ind(sample1, sample2)
print("\n--- Two-Sample t-Test ---")
print(f"T-statistic: {t:.2f}, P-value: {p:.4f}")
if p < 0.05:
 print("Reject H0")
else:
 print("Fail to reject H0")
observed = np.array([
 [30, 20], # Male preferences
 [40, 10] # Female preferences
])
chi, p, dof, expected = chi2_contingency(observed)
print("\n--- Chi-Square Test for Independence ---")
print(f"Chi-square Statistic: {chi:.2f}, P-value: {p:.4f}")
if p < 0.05:
 print("Conclusion:", "Reject H0")
else:
 print("Fail to reject H0")