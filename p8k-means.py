import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data =pd.read_csv(r"C:\Users\HP\OneDrive\Documents\DS practicals\Wholesale customers data.csv")
print(data.head())
categorical_features = ['Channel', 'Region']
continuous_features = ['Fresh', 'Milk', 'Grocery', 'Frozen','Detergents_Paper','Delicassen']
print(data[continuous_features].describe())
for col in categorical_features:
 dummies = pd.get_dummies(data[col], prefix=col)
 data = pd.concat([data, dummies], axis=1)
 data.drop(col, axis=1, inplace=True)
print(data.head())
mms = MinMaxScaler()
mms.fit(data)
data_transformed = mms.transform(data)
sum_of_squared_distances = []
K = range(1, 15)
for k in K:
 km = KMeans(n_clusters=k)
 km.fit(data_transformed) # You need to fit the model to the data first
 sum_of_squared_distances.append(km.inertia_) # Correct: inertia_ is an attribute, not a method
plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum of Squared Distances')
plt.title('Elbow Method for Optimal k')
plt.show()
optimal_k = 4 # Replace this with the value you choose based on the elbow method
km = KMeans(n_clusters=optimal_k)
km.fit(data_transformed)