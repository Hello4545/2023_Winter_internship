# Sleep duration
# nonclinical negative: sensitive related to short sleep duration
# clinical positive: sensitive related to long sleep duration)

import numpy as np

# 구현 필요: 핸드폰이 켜지는 시간 측정 https://developer.android.com/reference/android/app/usage/UsageStats

# Inputs
sleep_duration = 8 * 60 + 43
max_avg_sleep_duration = 8 * 60 + 22
min_avg_sleep_duration = 6 * 60
is_nonclinical = True
is_clinical = False
# nonclinical
max_range_nonclinical = 60
min_range_nonclinical = 30
max_sleep_duration_nonclinical = 12 * 60
min_sleep_duration_nonclinical = 4 * 60
# clinical
max_range_clinical = 30
min_range_clinical = 30
max_sleep_duration_clinical = 10 * 60 + 30
min_sleep_duration_clinical = 4 * 60

# Sleep duration calculation
if is_nonclinical:
    # nonclinical
    if sleep_duration in range(min_avg_sleep_duration, max_avg_sleep_duration + 1):
        score_sleep_duration = 0
    elif max_avg_sleep_duration < sleep_duration:
        score_sleep_duration = min(max_sleep_duration_nonclinical - max_avg_sleep_duration, sleep_duration - max_avg_sleep_duration) / (max_sleep_duration_nonclinical - max_avg_sleep_duration) * 100
    elif sleep_duration < min_avg_sleep_duration:
        score_sleep_duration = min(min_avg_sleep_duration - min_sleep_duration_nonclinical, min_avg_sleep_duration - sleep_duration) / (min_avg_sleep_duration - min_sleep_duration_nonclinical) * 100
else:
    # clinical
    if sleep_duration in range(min_avg_sleep_duration, max_avg_sleep_duration + 1):
        score_sleep_duration = 0
    elif max_avg_sleep_duration < sleep_duration:
        score_sleep_duration = min(max_sleep_duration_clinical - max_avg_sleep_duration, sleep_duration - max_avg_sleep_duration) / (max_sleep_duration_clinical - max_avg_sleep_duration) * 100
    elif sleep_duration < min_avg_sleep_duration:
        score_sleep_duration = min(min_avg_sleep_duration - min_sleep_duration_clinical, min_avg_sleep_duration - sleep_duration) / (min_avg_sleep_duration - min_sleep_duration_clinical) * 100
print(score_sleep_duration)

# continuous scale 대신 discrete scale의 경우
# if is_nonclinical:
#     # nonclinical
#     if sleep_duration in range(min_avg_sleep_duration, max_avg_sleep_duration + 1):
#         score_sleep_duration = 0
#     elif sleep_duration in range(min_avg_sleep_duration - min_range_nonclinical, 8 * 60 + max_range_nonclinical):
#         score_sleep_duration = 20
#     elif sleep_duration in range(min_avg_sleep_duration - 2 * min_range_nonclinical, 8 * 60 + 2 * max_range_nonclinical):
#         score_sleep_duration = 40
#     elif sleep_duration in range(min_avg_sleep_duration - 3 * min_range_nonclinical, 8 * 60 + 3 * max_range_nonclinical):
#         score_sleep_duration = 60
#     elif sleep_duration in range(min_avg_sleep_duration - 4 * min_range_nonclinical, 8 * 60 + 4 * max_range_nonclinical):
#         score_sleep_duration = 80
#     else:
#         score_sleep_duration = 100
# else:
#     # clinical
#     if sleep_duration in range(min_avg_sleep_duration, max_avg_sleep_duration + 1):
#         score_sleep_duration = 0
#     elif sleep_duration in range(min_avg_sleep_duration - min_range_clinical, 9 * 60):
#         score_sleep_duration = 20
#     elif sleep_duration in range(min_avg_sleep_duration - 2 * min_range_clinical, 9 * 60 + 1 * max_range_clinical):
#         score_sleep_duration = 40
#     elif sleep_duration in range(min_avg_sleep_duration - 3 * min_range_clinical, 9 * 60 + 2 * max_range_clinical):
#         score_sleep_duration = 60
#     elif sleep_duration in range(min_avg_sleep_duration - 4 * min_range_clinical, 9 * 60 + 3 * max_range_clinical):
#         score_sleep_duration = 80
#     else:
#         score_sleep_duration = 100
# print(score_sleep_duration)