import pandas as pd
#Reading a CSV file
df_csv = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\DS practicals\iris.csv')
print(df_csv.head())
# Reading a JSON file
df_json = pd.read_json(r'C:\Users\HP\OneDrive\Documents\DS practicals\iris.json')
print(df_json.head())
print(df_csv.isnull().sum())
print(df_csv.head())
df_csv['SepalWidthCm'].fillna(value=3,inplace=True) # Replace with a specific value
print(df_csv.head())
df_csv.dropna(inplace=True)
print(df_csv.head())
Q1 = df_csv['SepalWidthCm'].quantile(0.25)
Q3 = df_csv['SepalWidthCm'].quantile(0.75)
IQR = Q3 - Q1
df = df_csv[(df_csv['SepalWidthCm'] >= (Q1 - 1.5 * IQR)) & (df_csv['SepalWidthCm'] <= (Q3 + 1.5 * IQR))]
print("Outliers are: \n")
print(df)
filtered_df = df_csv[df_csv['SepalLengthCm'] > 5.0]
print(filtered_df)
sorted_df = df_csv.sort_values(by='PetalWidthCm', ascending=True)
print(sorted_df)
grouped_df = df_csv.groupby('Species')['PetalWidthCm'].sum()
print(grouped_df)