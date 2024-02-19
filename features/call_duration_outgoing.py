# Call duration (outgoing)

# 구현 필요: call log를 활용한 구현 --> 개발 과정에서 개선 필요

# Inputs
call_duration = 4
avg_call_duration = 4
min_call_duration = 0

# Call duration calculation
score_call_duration = max(avg_call_duration - call_duration, 0) / (avg_call_duration) * 100
print(score_call_duration)

# continuous scale 대신 discrete scale의 경우
# if 4 <= call_duration:
#     score_call_duration = 0
# elif 3 <= call_duration:
#     score_call_duration = 20
# elif 2 <= call_duration:
#     score_call_duration = 40
# elif 1 <= call_duration:
#     score_call_duration = 60
# elif 0 < call_duration:
#     score_call_duration = 80
# else:
#     score_call_duration = 100
# print(score_call_duration)