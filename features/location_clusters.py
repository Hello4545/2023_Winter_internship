# Location clusters: utilizes ML algorithm

# Location clusters는 ML algorithm 사용 필요 --> 개선 필요
# 구현 필요: Location variance, Location clusters는 우선 하나로 통합하여 판단 --> 개선 필요

# Inputs
# number of location clusters 구하는 방법 도입 필요
location_clusters = 3
avg_location_clusters = 5

# Location clusters calculation
score_location_clusters = (avg_location_clusters - min(location_clusters, avg_location_clusters)) / avg_location_clusters * 100
print(score_location_clusters)

# continuous scale 대신 discrete scale의 경우