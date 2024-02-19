# Entropy: Normalized entropy (sum of -p(logp))

import numpy as np
import math

# 구현 필요: location cluster 활용, time spent at each location 계산 필요

# Inputs
location_clusters = 3
waking_time = 16*60             # waking time과 time spent 일치 필요
time_spent_array = [180, 360, 420]    # cluster에 따라 소요한 시간 필요
percentage_array = []

# Entropy calculation
for i in range(location_clusters):
    percentage_array.append(time_spent_array[i]/waking_time)

entropy = sum(-p * math.log10(p) for p in percentage_array if p > 0)
avg_entropy = -(0.62 * math.log10(0.62) + 0.38 * math.log10(0.38)) / math.log10(2)
minimum_entropy = 0.55

if location_clusters != 1:
    # normalized entropy
    entropy = entropy / math.log10(location_clusters)

# print(entropy)
# score_entropy = 0

# score_entropy = max(0, min(avg_entropy - entropy, avg_entropy - minimum_entropy)) / (avg_entropy - minimum_entropy) * 100
score_entropy = (avg_entropy - max(minimum_entropy, min(avg_entropy, entropy))) / (avg_entropy - minimum_entropy) * 100
print(score_entropy)

# continuous scale 대신 discrete scale의 경우
# if avg_entropy <= entropy:
#     score_entropy = 0
# elif 0.85 <= entropy:
#     score_entropy = 20
# elif 0.75 <= entropy:
#     score_entropy = 40
# elif 0.65 <= entropy:
#     score_entropy = 60
# elif 0.55 <= entropy:
#     score_entropy = 80
# else:
#     score_entropy = 100
# print(score_entropy)