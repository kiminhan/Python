def ex(): '''
    하루동안에 3이 나타나는 시간을 초로 환사하면 총 몇초인지를 구하시오. 
    '''

help(ex)

sumSec=0    # 초의 총합을 저장할 변수
for hour in range(24) :     # 시간
    for minute in range(60) :   #분
        if '3' in str(hour) or '3' in str(minute) : # 시간이나 분에 3이 들어가면
            sumSec += 60            # 60초씩 더함
print("하루에", sumSec, "초 동안 3이 보입니다")

# def time():
#     count_hour = 0
#     count_min = 0
#     second = 60
#
#     # hour
#     for i in range(0,24):
#         if i == 3 or i == 13 or i == 23:
#             count_hour += 1
#         else:
#             continue
#
#     total_hour = count_hour * second * second
#
#     # min
#     for i in range(0,60):
#         if i == 3 or i == 13 or i == 23 or i == 43 or i == 53:
#             count_min += 1
#         elif 30 <= i < 40:
#             count_min += 1
#         else:
#             continue
#
#     total_min = count_min * second * 21
#
#     total_time = total_hour + total_min
#     return total_time
#
# print(time())