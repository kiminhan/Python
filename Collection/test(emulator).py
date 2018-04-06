import json
import random
import time

real_weather = []
real_weather_list = []

while True:
    go_to_weather = input("1. 계속할것입니까?   2. 종료할것입니까?\n입력해주세요: ")
    if go_to_weather == '1':
        real_weather ={   "baseDate": 20180129,
                "baseTime": 1430,
                "category": "RN1",
                "fcstDate": 20180129,
                "fcstTime": time.strftime("%H%M", time.localtime(time.time())),
                "fcstValue": random.randint(0,100),
                "nx": 89,
                "ny": 91
                }

    elif go_to_weather == '2':
        break

    real_weather_list.append(real_weather)

with open('weather.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(real_weather_list, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

# with open('weather.json', encoding='utf8') as outfile:
#     json_object = json.load(outfile)
#     json_string = json.dumps(json_object)
#     json_big_data = json.loads(json_string)
#
# weather_div = json_big_data[0]
# print(weather_div['fcstValue'])
