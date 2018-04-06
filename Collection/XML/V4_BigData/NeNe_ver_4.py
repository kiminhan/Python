#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import csv
import xml.etree.ElementTree as ET

nDivCnt = 100
result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv_w = ".csv"
record_limit = 12

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None

def make_nene(dir_index, file_index) :
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + str(file_index) + csv_w;
    filepath = 'E:\python.warkspace\Guri\XML\V4_BigData\V4_BigData\\Nene_Data1\\'
    fileName = 'nene'
    fileExe = '.csv'
    fileFolder = 'nene'
    nLineCnt = 0
    nFileIdx = 0
    f = open("%s" % (filepath + fileName + fileExe), 'r')
    fDivName = open("%s%02d%s" % (filepath + fileFolder, nFileIdx, fileExe), 'w')
    while True:
        line = f.readline()
        if not line: break

        if nLineCnt == nDivCnt:
            fDivName.close()
            nFileIdx += 1
            nLineCnt = 0
            strPat = "%s%02d%s" % (filepath + fileName, nFileIdx, fileExe)
            fDivName = open(strPat, 'w')
            print("생성 완료 %s" % strPat)
        nLineCnt += 1
        fDivName.write(line)

    fDivName.close()
    f.close()
    # nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

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

try : os.mkdir(dir_name)
except : pass
try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            make_dir(dir_index)

        make_nene(dir_index, file_index)
        file_index += 1

    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write(str(file_index))
except FileNotFoundError :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_nene(1, 1)

# filepath = 'E:\python.warkspace\Guri\XML\V4_BigData\\'
# fileName = 'nene'
# fileExe = '.csv'
# fileFolder = 'nene'

# nLineCnt = 0
# nFileIdx = 0
# f = open("%s" % (filepath + fileName + fileExe),'r')
# fDivName = open("%s%02d%s" % (filepath+fileFolder, nFileIdx, fileExe), 'w')
# while True:
#     line = f.readline()
#     if not line: break
#
#     if nLineCnt == nDivCnt:
#         fDivName.close()
#         nFileIdx += 1
#         nLineCnt = 0
#         strPat = "%s%02d%s" %(filepath+fileName, nFileIdx, fileExe)
#         fDivName = open(strPat,'w')
#         print("생성 완료 %s" % strPat)
#     nLineCnt += 1
#     fDivName.write(line)
#
# fDivName.close()
# f.close()

print("End")