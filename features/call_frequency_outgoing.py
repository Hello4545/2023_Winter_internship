# Call frequency (outgoing)

# 구현 필요: call log를 활용한 구현 --> 개발 과정에서 개선 필요

# Inputs
call_frequency = 10
avg_call_frequency = 8

# Call frequency calculation
score_call_frequency = max(avg_call_frequency - call_frequency, 0) / avg_call_frequency * 100
print(score_call_frequency)

# continuous scale 대신 discrete scale의 경우
# if 8 <= call_frequency:
#     score_call_frequency = 0
# elif 6 <= call_frequency:
#     score_call_frequency = 20
# elif 4 <= call_frequency:
#     score_call_frequency = 40
# elif 2 <= call_frequency:
#     score_call_frequency = 60
# elif 1 <= call_frequency:
#     score_call_frequency = 80
# else:
#     score_call_frequency = 100
# print(score_call_frequency)