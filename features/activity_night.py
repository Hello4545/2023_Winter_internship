# Activity Night

# 구현 필요: 가속도계 데이터로 뛰기, 걷기 구분하여 더 세밀한 측정 방법 도입 --> 개선 필요

# “Association between Daily Pattern of Physical Activity and Depression: A Systematic Review” 논문에서는 밤 시간을 오후 11시부터 오전 5시 30분까지로 규정
# (Activity Night) = (time active at night from 11:00PM to 05:30AM) / 6hrs 30mins x 100

from datetime import datetime, timedelta

# Inputs
night_start_time = datetime.strptime("2024-01-23 23:00", "%Y-%m-%d %H:%M")
night_end_time = datetime.strptime("2024-01-24 05:30", "%Y-%m-%d %H:%M")
total_night_time = (night_end_time - night_start_time).total_seconds()    # 11:00PM to 05:30AM

sleep_start_time = datetime.strptime("2024-01-24 01:00", "%Y-%m-%d %H:%M")
sleep_end_time = datetime.strptime("2024-01-24 10:00", "%Y-%m-%d %H:%M")

activity_night_start = max(night_start_time, sleep_start_time)
activity_night_end = min(night_end_time, sleep_end_time)
activity_night = total_night_time - (activity_night_end - activity_night_start).total_seconds()    # 11:00PM to 05:30AM

# Activity night calculation
score_activity_night = activity_night / total_night_time * 100
print(score_activity_night)

# continuous scale 대신 discrete scale의 경우