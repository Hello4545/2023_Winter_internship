# Screen active duration: how long the device's screen was active

import numpy as np

# 구현 필요: 핸드폰이 켜지는 시간 측정 https://developer.android.com/reference/android/app/usage/UsageStats

# Inputs
phone_active_duration = 226
other_screen_active_duration = 250
maximum_screen_active_duration = 600

screen_active_duration = phone_active_duration + other_screen_active_duration
avg_screen_active_duration = 397 # 6 hours 37 minutes

# Screen active duration calculation
score_screen_active_duration = min(maximum_screen_active_duration - avg_screen_active_duration, screen_active_duration - avg_screen_active_duration) / (maximum_screen_active_duration - avg_screen_active_duration) * 100
print(score_screen_active_duration)

# continuous scale 대신 discrete scale의 경우
# if screen_active_duration <= avg_screen_active_duration:
#     score_screen_active_duration = 0
# elif screen_active_duration <= 420:
#     score_screen_active_duration = 20
# elif screen_active_duration <= 480:
#     score_screen_active_duration = 40
# elif screen_active_duration <= 540:
#     score_screen_active_duration = 60
# elif screen_active_duration <= 600:
#     score_screen_active_duration = 80
# else:
#     score_screen_active_duration = 100
# print(score_screen_active_duration)