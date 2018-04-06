import json
import time
import datetime
import urllib.request

g_clock = False

Discomfort_number = []

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

def getClock(local_code,basetime):
    end_point="http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService2/getDsplsLifeList"

    parameters = "?_type=json&serviceKey="+access_key
    parameters+="&areaNo="+local_code
    parameters+="&time="+basetime

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_Clock_info():
    basetime = time.strftime("%Y%m%d%H", time.localtime(time.time()))
    basetime = int(basetime)
    basetime = str(basetime)
    local_code = '2714054000'

    jsondata = getClock(local_code,basetime)
    print(jsondata)
    jsonresult = jsondata['Response']['Body']['IndexModel']
    clock_div = jsonresult
    Discomfort_Index = len(clock_div)
    for i in range(Discomfort_Index):
        if 'h3' in clock_div[i]:
            Discomfort_number_list = clock_div[i]['h3']
            Discomfort_number.append(Discomfort_number_list)

    print(Discomfort_number[0])

get_realtime_Clock_info()