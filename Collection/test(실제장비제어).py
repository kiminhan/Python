import json
import time
import datetime
import urllib.request

REH_number = []
real_weather_list = []

access_key = "fgNUbFNWdrPsUqf6WsEPlsKYxDQ%2BgzRO2LIXFxVCeb7zMpjnDnIGiVINYnTenSQdMMseq9GIWW4Bkh5%2B7ZNXKA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getweather(basedate,basetime,nx,ny):
    end_point="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey="+access_key+"&numOfRows=100"
    parameters+="&base_date="+basedate
    parameters+="&base_time="+basetime
    parameters+="&nx="+nx
    parameters+="&ny="+ny

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_weather_info():
    jsonresult = []
    basedate = time.strftime("%Y%m%d", time.localtime(time.time()))
    basetime = time.strftime("%H%M", time.localtime(time.time()))
    basetime = int(basetime) - 100
    basetime = str(basetime)
    basetime = basetime.zfill(4)
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        jsonresult = jsondata['response']['body']['items']['item']
        weather_div = jsonresult
        REH_number_line = len(weather_div)
        for i in range(REH_number_line):
            if 'REH' in weather_div[i]['category']:
                REH_number_list = weather_div[i]['fcstValue']
                REH_number.append(REH_number_list)
        print(REH_number[0])

get_realtime_weather_info()

# weather_div = jsonresult
# REH_number_line = len(weather_div)
# for i in range(REH_number_line):
#     if 'REH' in weather_div[i]['category']:
#         REH_number_list = weather_div[i]['fcstValue']
#         REH_number.append(REH_number_list)
# print(REH_number[0])
