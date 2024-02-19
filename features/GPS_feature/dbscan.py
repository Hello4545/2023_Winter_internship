from cluster_feature import *
import os
from pathlib import Path

root_dir = os.path.dirname(Path(__file__).parent.parent)
data_dir = os.path.join(root_dir, "updated_data.csv")
data = pd.read_csv(data_dir)
data["obtained_at"] = pd.to_datetime(data["obtained_at"])
data["created_at"] = pd.to_datetime(data["created_at"])
selected_data = data[
    (data["obtained_at"].dt.year == 2024) & (data["obtained_at"].dt.month == 1)
]

coordinates = data[['latitude', 'longitude']]

# Use the DBSCAN algorithm for clustering
classifier = Classifier()
label_dbscan = classifier.DBSCAN(coordinates.values, rad=0.05, thres=3)

data['cluster'] = label_dbscan
num_clusters = len(set(label_dbscan)) - (1 if -1 in label_dbscan else 0)  # Exclude noise points (-1)
print(f'Number of clusters: {num_clusters}')

unique_labels, counts = np.unique(label_dbscan, return_counts=True)
counts_without_noise = counts[unique_labels != -1]
num_clusters_stay = np.sum(counts_without_noise > 5)

print(counts)

print(f'Number of clusters with more than 5 data points: {num_clusters_stay}')


# Plot and display the clusters
classifier.show_clusters(coordinates.values, label_dbscan)


# plt.scatter(data['longitude'], data['latitude'], alpha=0.5)
# plt.title('GPS Data Locations')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.show()

# # Create an instance of the Classifier
# classifier = Classifier()

# # Test DBSCAN on latitude and longitude data
# label = classifier.DBSCAN(coordinates, rad=4, thres=4)

# # Show the initial data
# classifier.show_clusters([coordinates], label)

# # Set parameters for the clusters
# # mu1 = [10, 10]
# # sigma1 = [[10, 5], [5, 10]]
# # N1 = 50

# # mu2 = [-10, -10]
# # sigma2 = [[10, -5], [-5, 10]]
# # N2 = 50

# # Create an instance of the ClusterGenerator and an instance of the Classifier
# cluster_gen = ClusterGenerator(seed=42)
# classifier = Classifier()

# # Create two clusters
# cluster1 = cluster_gen.generate_cluster(mu1, sigma1, N1)
# cluster2 = cluster_gen.generate_cluster(mu2, sigma2, N2)

# # Combine the clusters for DBSCAN testing
# combined_data = np.concatenate([cluster1, cluster2])

# # test DBSCAN
# label = classifier.DBSCAN(combined_data, rad=4, thres=4)

# # show the initial data
# cluster_gen.show_clusters([combined_data])

# # show the clusterd data
# classifier.show_clusters(combined_data, label)

# # show the true clusters
# cluster_gen.show_clusters([cluster1, cluster2])

# rad (radius): This parameter specifies the maximum distance between two samples for one to be considered as in the neighborhood of the other. In other words, it defines the radius of the neighborhood around each data point.

# thres (threshold): This parameter specifies the minimum number of data points required to form a dense region. It defines the threshold for the minimum number of points within the rad radius to consider a point as a core point.