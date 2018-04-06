#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
from pandas import DataFrame

def make_nene(index) :
    nene = "nene"
    csv = ".csv"
    nene_table.to_csv(nene + index + csv, encoding="cp949", mode='w', index=True)
    return None

result = []

import xml.etree.ElementTree as ET
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

try :
    with open("nene_index.txt", 'r') as file :
        index = file.readline()
        make_nene(index)
        index = int(index)
        index += 1
        index = str(index)
    with open("nene_index.txt", 'w') as file :
        file.write(index)
except FileNotFoundError :
    with open("nene_index.txt", 'w') as file :
        file.write('2')

make_nene('1')

print("End")