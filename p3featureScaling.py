import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
# Load Titanic Dataset
titanic = sns.load_dataset("titanic")
# Drop rows with missing values for simplicity
titanic = titanic.dropna()
# Identify numerical and categorical columns
numerical_columns = ['age', 'fare']
categorical_columns = ['sex', 'embarked', 'class']
# Standardization
standard_scaler = StandardScaler()
titanic_standardized = titanic.copy()
titanic_standardized[numerical_columns] = standard_scaler.fit_transform
(titanic[numerical_columns])
# Normalization
min_max_scaler = MinMaxScaler()
titanic_normalized = titanic.copy()
titanic_normalized[numerical_columns] = min_max_scaler.fit_transform
(titanic[numerical_columns])
# Dummification
titanic_dummified = pd.get_dummies(titanic, columns=categorical_columns,
 drop_first=True)
# Save Results
titanic_standardized.to_csv("titanic_standardized.csv", index=False)
titanic_normalized.to_csv("titanic_normalized.csv", index=False)
titanic_dummified.to_csv("titanic_dummified.csv", index=False)
# Display Results
print("Standardized Data:\n", titanic_standardized.head())
print("\nNormalized Data:\n", titanic_normalized.head())
print("\nDummified Data:\n", titanic_dummified.head())