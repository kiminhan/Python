import csv

def get_csv_row_Instance(row_name) :
    row_instance = []
    row_index = data[0].index(row_name)
    for row in data[1:]:
        row_instance.append(row[row_index])
    return row_instance

def get_csv_col_Instance(primary_key) :
    for primary_key_instance in data[1:]:
        if primary_key_instance[0] == primary_key : return primary_key_instance
        else : continue

def print_col(primary_key_instance) :
    counting = 0
    print("행의 데이터는 아래와 같습니다.")
    try :
        for x in primary_key_instance :
            print("%s : %-10s" %(data[0][counting], x), end ='' )
        print()
        return 0
    except TypeError :
        print("찾는 Primaty_key가 없습니다.")
        return 1

def check_type(row_instance):
        try:
            for i in range(len(row_instance)):
                row_instance[i] = int(row_instance[i])
        except:
            for i in range(len(row_instance)):
                row_instance[i] = float(row_instance[i])
        return row_instance

def my_sum(row_instance):
    sum = 0
    for i in row_instance:
        sum += i
    return sum

def my_averge(row_instance):
    total = my_sum(row_instance)
    averge = total / len(row_instance)
    return averge

def my_max(row_instance):
    return max(row_instance)

def my_min(row_instance):
    return min(row_instance)

def my_deviation(row_instance):
    dev_element = my_averge(row_instance)
    dev_element = dev_element
    for i in row_instance:
        print(i,"-",dev_element,"=",i-dev_element)

# def my_standard_devuation(row_instance):
# def my_variance(row_instance):
#     dev_element = my_averge(row_instance)
#     dev_element = dev_element
#     i = []
#     for i in row_instance:
#         var_element = i*i
#         var_sum = []
#         for j in var_element:
#             var_sum += j
#             return var_sum

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file :
    data = list(csv.reader(file))

while 1 :
    access_type = input("Access 데이터 유형을 선택하십시오.(1:행 2:열 3:총합 4:평균 5:최대값 6:최소값 7:편차 8:표준편차 9:분산 28:종료) : ")
    if access_type == '28' : break
    elif access_type == '1' :
        search_primary_key = input("Access하려는 Primary_key를 입력하세요. : ")
        print_col(get_csv_col_Instance(search_primary_key))
    elif access_type == '2' :
        search_row_info = input("찾고싶은 Primary_key와 출력타입(기본은 int형)을 입력하십시오.").split(', ')
        print_type = ""
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info[0])
        print(row_instance)
    elif access_type == '3' :
        search_row_info = input("총합을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_sum(check_type(row_instance)))
    elif access_type == '4' :
        search_row_info = input("평균을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_averge(check_type(row_instance)))
    elif access_type == '5' :
        search_row_info = input("최대값을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_max(check_type(row_instance)))
    elif access_type == '6' :
        search_row_info = input("최소값을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_min(check_type(row_instance)))
    elif access_type == '7' :
        search_row_info = input("편차값을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_deviation(check_type(row_instance)))
    elif access_type == '8' :
        search_row_info = input("표준편차값을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print((check_type(row_instance)))
    elif access_type == '9' :
        search_row_info = input("분산값을 구하고싶은 Primary_key를 입력하십시오 : ")
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info)
        print(my_variance(check_type(row_instance)))

