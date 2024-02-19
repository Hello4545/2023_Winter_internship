import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


class GPSfeatures:
    def __init__(self):
        pass

    def location_variance(self, data):
        longitude_variance = data["longitude"].std()
        latitude_variance = data["latitude"].std()
        return longitude_variance

    def total_distance(self, data):
        longitude_variance = data["longitude"].std()
        latitude_variance = data["latitude"].std()
        return longitude_variance
        # diff_longitude = (data["longitude"].diff()).drop([0])
        # diff_latitude = (data["latitude"].diff()).drop([0])
        # return np.sum(np.sqrt(np.square(diff_longitude) + np.square(diff_latitude)))
    
    # 개선 필요: speed로 GPS 데이터 걸러내는 작업 필요
    def speed(self, data):
        diff_longitude = (data["longitude"].diff()).drop([0])
        diff_latitude = (data["latitude"].diff()).drop([0])
        diff_time = (data["obtained_at"].diff()).drop([0]) / pd.Timedelta(seconds=1)
        diff_longitude = diff_longitude[diff_time != 0]
        diff_latitude = diff_latitude[diff_time != 0]
        diff_time = diff_time[diff_time != 0]
        return np.sqrt(
            np.square(diff_longitude / diff_time) + np.square(diff_latitude / diff_time)
        )
    
    def speed_in_km(self, data):
        diff_longitude = (data["longitude"].diff()).drop([0])
        diff_latitude = (data["latitude"].diff()).drop([0])
        diff_time = (data["obtained_at"].diff()).drop([0]) / pd.Timedelta(seconds=1)
        diff_longitude = diff_longitude[diff_time != 0]
        diff_latitude = diff_latitude[diff_time != 0]
        diff_time = diff_time[diff_time != 0]
        return np.sqrt(
            np.square(diff_longitude / diff_time) + np.square(diff_latitude / diff_time)
        )

    def speed_mean(self, data):
        return np.mean(self.speed(data))

    def speed_variance(self, data):
        return np.std(self.speed(data))
