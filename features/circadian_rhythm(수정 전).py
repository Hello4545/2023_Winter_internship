# Circadian rhythm (consistency of total sleep time)
# weekday와 weekend 구분한 경우

import numpy as np
from datetime import datetime, timedelta

# 구현 필요: 수면 시간 측정

# Inputs
# weekdays
avg_total_sleep_time_wk = 12 * 60 * 60    # Average TST로 할지 total range of sleep time으로 할지 고민 필요
init_time_wk = ['2024-01-21 23:12:12', '2024-01-22 23:10:12']  #'%Y-%m-%d %H:%M:%S'
end_time_wk = ['2024-01-22 10:12:12', '2024-01-23 9:9:11']  #'%Y-%m-%d %H:%M:%S'

# weekend
avg_total_sleep_time_wd = 12 * 60 * 60    # Average TST로 할지 total range of sleep time으로 할지 고민 필요
init_time_wd = ['2024-01-21 02:12:12', '2024-01-22 01:10:12']  #'%Y-%m-%d %H:%M:%S'
end_time_wd = ['2024-01-22 10:12:12', '2024-01-23 9:9:11']  #'%Y-%m-%d %H:%M:%S'

# Converting string representations of time to datetime objects
# init_time = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time(), init_time))
# end_time = list(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time(), end_time))
# init_time = [datetime.strptime(time.split()[1], '%H:%M:%S') for time in init_time]
# end_time = [datetime.strptime(time.split()[1], '%H:%M:%S') for time in end_time]

# weekdays
init_time_wk = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in init_time_wk]
end_time_wk = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in end_time_wk]

# weekend
init_time_wd = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in init_time_wd]
end_time_wd = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time() for time in end_time_wd]

# Maximum and minimum timestamps
# max_init_time = max(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time().strftime('%H:%M:%S'), init_time))
# min_end_time = min(map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time().strftime('%H:%M:%S'), end_time))
# weekdays
max_init_time_wk = max(init_time_wk)
min_end_time_wk = min(end_time_wk)

# weekend
max_init_time_wd = max(init_time_wd)
min_end_time_wd = min(end_time_wd)

# Overlap time
# overlap_time = datetime.combine(datetime.today(), min_end_time) - datetime.combine(datetime.today(), max_init_time)
# weekdays
overlap_time_wk = timedelta(hours=min_end_time_wk.hour, minutes=min_end_time_wk.minute, seconds=min_end_time_wk.second) - timedelta(hours=max_init_time_wk.hour, minutes=max_init_time_wk.minute, seconds=max_init_time_wk.second)
overlap_time_wk = str(overlap_time_wk).split(", ")[-1]
overlap_time_wk = datetime.strptime(overlap_time_wk, '%H:%M:%S').time()
overlap_time_wk = (overlap_time_wk.hour * 60 + overlap_time_wk.minute) * 60 + overlap_time_wk.second
# overlap_timedelta = timedelta(hours=min_end_time.hour - max_init_time.hour, minutes=min_end_time.minute - max_init_time.minute, seconds=min_end_time.second - max_init_time.second)
# overlap_seconds = overlap_time.total_seconds() % (24 * 3600)

# weekend
overlap_time_wd = timedelta(hours=min_end_time_wd.hour, minutes=min_end_time_wd.minute, seconds=min_end_time_wd.second) - timedelta(hours=max_init_time_wd.hour, minutes=max_init_time_wd.minute, seconds=max_init_time_wd.second)
overlap_time_wd = str(overlap_time_wd).split(", ")[-1]
overlap_time_wd = datetime.strptime(overlap_time_wd, '%H:%M:%S').time()
overlap_time_wd = (overlap_time_wd.hour * 60 + overlap_time_wd.minute) * 60 + overlap_time_wd.second

# Circadian rhythm calculation
# weekdays
overlap_ratio_wk = overlap_time_wk / avg_total_sleep_time_wk * 100

# weekend
overlap_ratio_wd = overlap_time_wd / avg_total_sleep_time_wd * 100

overlap_ratio = 0.5 * overlap_ratio_wk + 0.5 * overlap_ratio_wd
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