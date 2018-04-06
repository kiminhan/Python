#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

name = "nene"
csv = ".csv"
data = "V2_BigData"
div = "\\"
data_div = "Name_Data"
record_rimit = 3

try:
    os.mkdir(data)
except:pass

try:
    with open(data+div+"nene_index.txt",'r') as f:
        index = f.readline()
        index = int(index)
        data_div_number = int(index/record_rimit)
        if index % record_rimit != 0:
            data_div_number = data_div_number + 1
        if index % record_rimit == 1:
            os.mkdir(data + div + data_div+str(data_div_number))
    address_sum = data + div + data_div + str(data_div_number) + div + name + str(index) + csv
    nene_table.to_csv(address_sum, encoding="cp949", mode='w', index=True)
    index += 1
    with open(data+div+"nene_index.txt", 'w') as f:
        f.write(str(index))
except:
    with open(data+div+"nene_index.txt", 'w') as f:
        f.write("2")
    os.mkdir(data+div+data_div+"1")
    nene_table.to_csv(data + div + data_div + "1" + div + name + "1" + csv, encoding="cp949", mode='w', index=True)

print("End")