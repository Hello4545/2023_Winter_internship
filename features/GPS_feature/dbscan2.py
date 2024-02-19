import pandas as pd
from cluster_feature import *
import os
from pathlib import Path
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

root_dir = os.path.dirname(Path(__file__).parent.parent)
data_dir = os.path.join(root_dir, "updated_data.csv")
data = pd.read_csv(data_dir)
data["obtained_at"] = pd.to_datetime(data["obtained_at"])
data["created_at"] = pd.to_datetime(data["created_at"])
selected_data = data[
    (data["obtained_at"].dt.year == 2024) & (data["obtained_at"].dt.month == 1)
]

# Extract latitude and longitude columns
coordinates = data[['latitude', 'longitude']]

scaler = StandardScaler()
coordinates_scaled = scaler.fit_transform(coordinates)

from sklearn.cluster import DBSCAN

# Choose appropriate epsilon and min_samples values
epsilon = 0.3  # Distance threshold
min_samples = 1  # Minimum number of points to form a dense region

dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
clusters = dbscan.fit_predict(coordinates_scaled)

# Add the cluster labels to the original dataframe
data['cluster'] = clusters
num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)  # Exclude noise points (-1)
print(f'Number of clusters: {num_clusters}')


# print(data[['longitude', 'latitude', 'cluster']])

plt.scatter(data['longitude'], data['latitude'], c=data['cluster'], cmap='tab10', s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('DBSCAN Clusters')
plt.show()
# Display the data with cluster labels

