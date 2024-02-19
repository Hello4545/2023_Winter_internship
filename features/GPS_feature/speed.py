from gps_feature import *
import os
from pathlib import Path

root_dir = os.path.dirname(Path(__file__).parent.parent)
data_dir = os.path.join(root_dir, "updated_data.csv")
data = pd.read_csv(data_dir)
data["obtained_at"] = pd.to_datetime(data["obtained_at"])
data["created_at"] = pd.to_datetime(data["created_at"])

# Select data of a specific date
selected_data = data[
    (data["obtained_at"].dt.year == 2024) & (data["obtained_at"].dt.month == 1)
]

feature = GPSfeatures()

# Calculate the speed mean of the selected data
speed = feature.speed(selected_data)
# speed_in_km = 
print("Calculate the speed mean")
print(speed)
