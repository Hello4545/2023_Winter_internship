# Energy expense
# uses step count from GoogleFit https://developers.google.com/android/reference/com/google/android/gms/fitness/RecordingClient

import numpy as np
import math

# 구현 필요: Energy expense를 명확히 측정할 수 있는 방법 도입 필요 --> 개선 필요

# 1. (하루 평균 섭취량) – (하루 평균 기초대사량)을 100으로 생각하여 소모되어야 하는 열량으로 생각 삼성 헬스 등 칼로리 소모량을 측정할 수 있는 API가 있다면 도입, 없을 경우 사용자가 직접 입력
# 2. 평균 운동 시간이나 운동 시간표로 계산 (사용자가 직접 입력)
# 3. 단순히 걸음 수와 똑같이 생각

# 아래 코드는 단순히 운동 기준표로 측정

# Inputs
exercise_time = 40
intensity_arr = [0, 1, 2, 3, 4, 5]
exercise_intensity = intensity_arr[3]

# Energy expense calculation
# continous scale?

# continuous scale 대신 discrete scale의 경우
if 90 <= exercise_time or 4 <= exercise_intensity:
    score_energy_expense = 0
elif 60 <= exercise_time or 3 <= exercise_intensity < 4:
    score_energy_expense = 20
elif 30 <= exercise_time or 2 <= exercise_intensity < 3:
    score_energy_expense = 40
elif 15 <= exercise_time or 1 <= exercise_intensity < 2:
    score_energy_expense = 60
elif 0 < exercise_time < 15 or 0 < exercise_intensity < 1:
    score_energy_expense = 80
else:
    score_energy_expense = 100
print(score_energy_expense)

# 하루 평균 1시간 30분 이상 운동 혹은 힘든 운동을 함: 0
# 하루 평균 1시간 이상 운동 혹은 격렬한 운동을 함: 20
# 하루 평균 30분 이상 운동 혹은 중간/가벼운 정도의 운동을 함: 40
# 하루 평균 15분 이상 30분 이하 운동 혹은 가벼운 운동을 함: 60
# 운동을 거의 하지 않음: 80
# 운동을 전혀 하지 않음/활동을 하지 않음: 100
# 추후 조정이 필요하면 조정 예정