import time

# print(time.strftime("%H%M", time.localtime(time.time())))
AI_time = time.localtime(time.time())
#             if AI_time[4] == 45 and AI_time[5] == 30:
print(AI_time)
time_min = time.strftime("%M%S")
print(time_min)
print(type(time_min))
