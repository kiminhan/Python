import csv

def get_csv_col_instance(primary_key):
    for primary_key_instance in data[1:]:
        if primary_key_instance[0] == primary_key : return primary_key_instance
        else: continue

def print_col(primary_key_instance):
    counting = 0
    print("행의 데이터는 아래와 같습니다.")
    try:
        for x in primary_key_instance:
            print("%s : %s" %(data[0][counting], x))
            counting += 1
        print()
        return 0
    except TypeError:
        print("찾는 primary_key가 없습니다.")
        return 1

def get_csv_row_instance(row_name):
    row_instance = []
    row_index = data[0].index(row_name)
    for row in data[1:]:
        row_instance.append(row[row_index])
    return row_instance

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file:
    data = list(csv.reader(file))

while 1:
    access_type = input("Access 유형을 선택해주세요. (1:행 2:열 3: 종료) : ")
    if access_type == '3' : break
    elif access_type == '1':
        search_primary_key = input("Access하려는 primary_key를 입력하세요 : ")
        print_col(get_csv_col_instance(search_primary_key))
    elif access_type == '2':
        search_row_info = input("찾고싶은 primary_key를 입력하세요.").split(', ')
        print_type = ""
        try:
            print_type = search_row_info[1]
        except:
            print_type = "int"
        row_instance = get_csv_row_instance(search_row_info[0])
        print(row_instance)
        #