# Location variance

# 구현 필요: Location variance, Location clusters는 우선 하나로 통합하여 판단 --> 개선 필요

# Location clusters: utilizes ML algorithm

# Inputs
# number of location clusters 구하는 방법 도입 필요
location_clusters = 3
avg_location_clusters = 5

# Location clusters calculation
score_location_clusters = (avg_location_clusters - max(location_clusters, avg_location_clusters)) / avg_location_clusters * 100
print(score_location_clusters)

# continuous scale 대신 discrete scale의 경우
# if 5000 <= step_count:
#     score_activity = 0
# elif 4000 <= step_count:
#     score_activity = 20
# elif 3000 <= step_count:
#     score_activity = 40
# elif 2000 <= step_count:
#     score_activity = 60
# elif 1000 <= step_count:
#     score_activity = 80
# else:
#     score_activity = 100
# print(score_activity)