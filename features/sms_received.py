# SMS received

# 구현 필요: SMS log를 활용한 구현 --> 개발 과정에서 개선 필요

# Inputs
SMS_received = 40
max_SMS_received = 50
min_SMS_received = 10

# SMS_received calculation
score_SMS_received = min(max_SMS_received - min_SMS_received, max(max_SMS_received - SMS_received, 0)) / (max_SMS_received - min_SMS_received) * 100
print(score_SMS_received)

# continuous scale 대신 discrete scale의 경우
# if 50 <= SMS_received:
#     score_SMS_received = 0
# elif 40 <= SMS_received:
#     score_SMS_received = 20
# elif 30 <= SMS_received:
#     score_SMS_received = 40
# elif 20 <= SMS_received:
#     score_SMS_received = 60
# elif 10 <= SMS_received:
#     score_SMS_received = 80
# else:
#     score_SMS_received = 100
# print(score_SMS_received)