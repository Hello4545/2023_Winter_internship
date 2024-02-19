# Vigorous activity
# uses step count from GoogleFit https://developers.google.com/android/reference/com/google/android/gms/fitness/RecordingClient

import numpy as np
import math

# 구현 필요: Activity, Vigorous activity는 우선 하나로 통합하여 걸음 수로 판단 --> 개선 필요

# Inputs
step_count = 4300
avg_step_count = 4898

# Vigorous activity calculation
score_vigorous_activity = max(0, avg_step_count - step_count) / avg_step_count * 100
print(score_vigorous_activity)

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