# Home stay: percentage of waking time spent at home

import numpy as np

# 구현 필요: GPS 상으로 home에 있는 시간 측정 필요

# Inputs
time_at_home = 800
waking_time = 16*60

# Home stay calculation
home_stay = time_at_home / waking_time * 100
avg_home_stay = 62

score_home_stay = max(0, home_stay - avg_home_stay) / (100 - avg_home_stay) * 100
print(score_home_stay)

# continuous scale 대신 discrete scale의 경우
# if home_stay <= 62:
#     score_home_stay = 0
# elif home_stay <= 69.6:
#     score_home_stay = 20
# elif home_stay <= 77.2:
#     score_home_stay = 40
# elif home_stay <= 84.8:
#     score_home_stay = 60
# elif home_stay <= 92.4:
#     score_home_stay = 80
# else:
#     score_home_stay = 100
# print(score_home_stay)