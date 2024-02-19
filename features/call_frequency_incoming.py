# Call frequency (incoming)

# 구현 필요: call log를 활용한 구현 --> 개발 과정에서 개선 필요

# Inputs
call_frequency = 10
avg_call_frequency = 8
max_call_frequency = 15
min_call_frequency = 5

# Call frequency calculation
score_call_frequency = min(max_call_frequency - min_call_frequency, max(call_frequency - min_call_frequency, 0)) / (max_call_frequency - min_call_frequency) * 100
print(score_call_frequency)

# continuous scale 대신 discrete scale의 경우
# if call_frequency <= 5:
#     score_call_frequency = 0
# elif call_frequency <= 8:
#     score_call_frequency = 20
# elif call_frequency <= 10:
#     score_call_frequency = 40
# elif call_frequency <= 12:
#     score_call_frequency = 60
# elif call_frequency <= 14:
#     score_call_frequency = 80
# else:
#     score_call_frequency = 100
# print(score_call_frequency)