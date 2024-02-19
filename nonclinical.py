# Calculation of the depression score (index) of the nonclinical

# Import necessary libraries
import numpy as np

# Product of weight direction and % of significant studies
product_array = [0.75, 0.6298, 0.0075, -0.84, -0.33, -1, -0.67, -0.5, -0.1632, -0.5963]
# order = index_home_stay, index_screen_active_duration, index_screen_active_frequency,
# index_entropy, index_activity, index_circadian_rhythm, index_variance,
# index_vigorous_activity, index_location_clusters, index_sleep_duration

# Normalized product
normalized_product_array = [p / sum(map(abs, product_array)) if p >= 0 else -p / sum(map(abs, product_array)) for p in product_array]

# indices of positive and negative feature of depression (nonclinical)
index_array = [i / sum(normalized_product_array) for i in normalized_product_array]

# index_home_stay = 0.136691696, index_screen_active_duration = 0.114784574, index_screen_active_frequency = 0.001366917, index_entropy = 0.1530947, index_activity = 0.060144346, index_circadian_rhythm = 0.182255595, index_variance = 0.122111249, index_vigorous_activity = 0.091127798, index_location_clusters = 0.029744113, index_sleep_duration = 0.108679011
# index_array = [index_home_stay, index_screen_active_duration, index_screen_active_frequency,
#                index_entropy, index_activity, index_circadian_rhythm, index_variance,
#                index_vigorous_activity, index_location_clusters, index_sleep_duration]

# Scores
score_home_stay = 1
score_screen_active_duration = 1
score_screen_active_frequency = 1
score_entropy = 1
score_activity = 1
score_circadian_rhythm = 1
score_variance = 1
score_vigorous_activity = 1
score_location_clusters = 1
score_sleep_duration = 1
# score_home_stay = 0.136691696
# score_screen_active_duration = 0.114784574
# score_screen_active_frequency = 0.001366917
# score_entropy = 0.1530947
# score_activity = 0.060144346
# score_circadian_rhythm = 0.182255595
# score_variance = 0.122111249
# score_vigorous_activity = 0.091127798
# score_location_clusters = 0.029744113
# score_sleep_duration = 0.108679011

score_array = [score_home_stay, score_screen_active_duration, score_screen_active_frequency,
               score_entropy, score_activity, score_circadian_rhythm, score_variance,
               score_vigorous_activity, score_location_clusters, score_sleep_duration]

# Score calculation
depression_score = np.dot(index_array, score_array)
print(depression_score)
