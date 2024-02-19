import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from cluster_feature import *

root_dir = os.path.dirname(Path(__file__).parent.parent)
data_dir = os.path.join(root_dir, "updated_data.csv")
data = pd.read_csv(data_dir)
data['obtained_at'] = pd.to_datetime(data['obtained_at'])
data['created_at'] = pd.to_datetime(data['created_at'])

# Plot the locations
plt.scatter(data['longitude'], data['latitude'], alpha=0.5)
plt.title('GPS Data Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# # Instantiate the Classifier
# classifier = Classifier()

# # Call the DBSCAN method
# labels = classifier.DBSCAN(data, rad=3, thres=4)

# # Plot the clusters
# classifier.plot_clusters(data, labels)

# # Additional code (if needed):
# # speed = classifier.speed(selected_data)

# print(data.dtypes)