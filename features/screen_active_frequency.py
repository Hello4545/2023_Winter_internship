# Screen active frequency: how many times screen was active

import numpy as np

# 구현 필요: 핸드폰이 켜지는 횟수 측정 https://developer.android.com/reference/android/app/usage/UsageStats

# Inputs
screen_active_frequency = 67
avg_screen_active_frequency = 58
range = 40

# Screen active frequency calculation
score_screen_active_frequency = min(range, screen_active_frequency - avg_screen_active_frequency) / range * 100
print(score_screen_active_frequency)

# continuous scale 대신 discrete scale의 경우
# if screen_active_frequency <= avg_screen_active_frequency:
#     score_screen_active_frequency = 0
# elif screen_active_frequency <= avg_screen_active_frequency + range / 4:
#     score_screen_active_frequency = 20
# elif screen_active_frequency <= avg_screen_active_frequency + 2 * range / 4:
#     score_screen_active_frequency = 40
# elif screen_active_frequency <= avg_screen_active_frequency + 3 * range / 4:
#     score_screen_active_frequency = 60
# elif screen_active_frequency <= avg_screen_active_frequency + 4 * range / 4:
#     score_screen_active_frequency = 80
# else:
#     score_screen_active_frequency = 100
# print(score_screen_active_frequency)