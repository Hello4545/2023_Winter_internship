# Call duration (incoming)

# 구현 필요: call log를 활용한 구현 --> 개발 과정에서 개선 필요

# Inputs
call_duration = 10
avg_call_duration = 4
max_call_duration = 30

# Call duration calculation
score_call_duration = min(max_call_duration - avg_call_duration, max(call_duration - avg_call_duration, 0)) / (max_call_duration - avg_call_duration) * 100
print(score_call_duration)

# continuous scale 대신 discrete scale의 경우
# if call_duration <= 4:
#     score_call_duration = 0
# elif call_duration <= 10:
#     score_call_duration = 20
# elif call_duration <= 15:
#     score_call_duration = 40
# elif call_duration <= 20:
#     score_call_duration = 60
# elif call_duration <= 25:
#     score_call_duration = 80
# else:
#     score_call_duration = 100
# print(score_call_duration)