# Circadian rhythm (consistency of total sleep time)

import numpy as np
from datetime import datetime, timedelta

# 구현 필요: 수면 시간 측정

# Inputs
avg_total_sleep_time = 12 * 60 * 60    # Average TST로 할지 total range of sleep time으로 할지 고민 필요
init_time = ['2024-01-21 23:12:12', '2024-01-22 23:10:12']  #'%Y-%m-%d %H:%M:%S'
end_time = ['2024-01-22 10:12:12', '2024-01-23 9:9:11']  #'%Y-%m-%d %H:%M:%S'

# Converting string representations of time to datetime objects
# init_time = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time(), init_time))
# end_time = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time(), end_time))
# init_time = [datetime.strptime(time.split()[1], '%H:%M:%S') for time in init_time]
# end_time = [datetime.strptime(time.split()[1], '%H:%M:%S') for time in end_time]
init_time = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in init_time]
end_time = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in end_time]

# Maximum and minimum timestamps
# max_init_time = max(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time().strftime('%H:%M:%S'), init_time))
# min_end_time = min(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time().strftime('%H:%M:%S'), end_time))
max_init_time = max(init_time)
min_end_time = min(end_time)

# Overlap time
# overlap_time = datetime.combine(datetime.today(), min_end_time) - datetime.combine(datetime.today(), max_init_time)
overlap_time = timedelta(hours=min_end_time.hour, minutes=min_end_time.minute, seconds=min_end_time.second) - timedelta(hours=max_init_time.hour, minutes=max_init_time.minute, seconds=max_init_time.second)
overlap_time = str(overlap_time).split(", ")[-1]
overlap_time = datetime.strptime(overlap_time, '%H:%M:%S').time()
overlap_time = (overlap_time.hour * 60 + overlap_time.minute) * 60 + overlap_time.second
# overlap_timedelta = timedelta(hours=min_end_time.hour - max_init_time.hour, minutes=min_end_time.minute - max_init_time.minute, seconds=min_end_time.second - max_init_time.second)
# overlap_seconds = overlap_time.total_seconds() % (24 * 3600)

# Circadian rhythm calculation
overlap_ratio = overlap_time / avg_total_sleep_time * 100
score_circadian_rhythm = max(0, 100 - overlap_ratio)
print(score_circadian_rhythm)

# continuous scale 대신 discrete scale의 경우
# if 90 <= overlap_ratio:
#     score_circadian_rhythm = 0
# elif 80 <= overlap_ratio:
#     score_circadian_rhythm = 20
# elif 60 <= overlap_ratio:
#     score_circadian_rhythm = 40
# elif 40 <= overlap_ratio:
#     score_circadian_rhythm = 60
# elif 20 <= overlap_ratio:
#     score_circadian_rhythm = 80
# else:
#     score_circadian_rhythm = 100
# print(score_circadian_rhythm)