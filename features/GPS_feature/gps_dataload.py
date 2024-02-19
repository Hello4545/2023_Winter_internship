import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import json

root_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(root_dir, "data.csv")

# Read existing data from data.csv
old_data = pd.read_csv(file_dir)

# Creating a DataFrame with the specified column names
new_data = pd.DataFrame(old_data)

# Appending the existing data to the new DataFrame
new_data = pd.concat([new_data], axis=1)

# Save the updated DataFrame to a new CSV file
new_data.to_csv("updated_data.csv", header=["index", "longitude", "latitude", "obtained_at", "created_at", "number"])
