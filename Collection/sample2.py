import json

student_result = []
student_list = []
student_information = []

address_file = 'ITT_Student.json'
address = ''

try:
    with open(address_file, encoding='utf8') as outfile:
        json_object = json.load(outfile)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        student_list = json_big_data
except FileNotFoundError:
    file_maker = input('''경로에 파일이 없습니다. 어떻게 하시겠습니까?
    1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.
    메뉴를 선택하세요 : ''')
    address_file = '\ITT_Student.json'
    if file_maker == '1':
        address = input("경로를 입력해주세요 : ")
        with open(address + address_file ,encoding='utf8') as outfile:
            json_object = json.load(outfile)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
    elif file_maker == '2':
        address_file = 'ITT_Student.json'
        address = ''

while True:
    student_management = input("""<< json기반 주소록 관리 프로그램 >>
1. 학생 정보입력
2. 학생 정보조회
3. 학생 정보수정
4. 학생 정보삭제
5. 프로그램 종료
    입력 : """)
    if student_management == '5':
        break
    elif student_management == '1':
        student_information = {
            'student_ID': "ITT" + '{:0=3}'.format(len(student_information)+1),
            'name': input("성함은? : "),
            'age': input("나이는? : "),
            'address': input("주소는? : "),
            'lecture_information':
                {
                'past_lecture_subject': input("과거수강횟수는? : "),
                'recent_lecture_subject':
                    [
                    {
                    'lecture_code':input("강의코드는? : "),
                    'lecture_name':input("강의명? : "),
                    'teacher':input("강사는? : "),
                    'start_day':input("개강일은? : "),
                    'close_day':input("종료일은? : ")
                    }
                    ]
                }
            }
        student_result.append(student_information)
    elif student_management == '2':
        student_list += student_result
        for i in range(len(student_list)):
            recent_lecture_list = student_list[i]['lecture_information']['recent_lecture_subject']
            print("학생ID : ",student_list[i]['student_ID'])
            print("이름 : ",student_list[i]['name'])
            print("나이 : ",student_list[i]['age'])
            print("주소 : ",student_list[i]['address'])
            print("과거수강횟수 : ",student_list[i]['lecture_information']['past_lecture_subject'])
            print("현재수강과목")
            print(" - 강의코드 : ",recent_lecture_list[0]['lecture_code'])
            print(" - 강의명 : ",recent_lecture_list[0]['lecture_name'])
            print(" - 강사 : ", recent_lecture_list[0]['teacher'])
            print(" - 개강일 : ", recent_lecture_list[0]['start_day'])
            print(" - 종강일 : ", recent_lecture_list[0]['close_day'])

student_list += student_result
with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(student_list, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

# import json
#
# jsonResult = []
# json_Result_1 = []
# json_Result_2 = []
# json_Result_3 = []
# g_json_bigdata = []
#
# file_address = ''
# file_address_name = 'ITT_student.json'
#
# try:
#     with open('ITT_student.json',encoding='utf8') as outfile:
#         json_object = json.load(outfile)
#         json_string = json.dumps(json_object)
#         json_big_data = json.loads(json_string)
#         json_Result_2 = json_big_data
# except:
#     print("파일이 없습니다.")
#     file_maker = input("""1.파일경로를 입력    2.신규생성
# 입력해주세요 : """)
#     if file_maker == '1':
#         file_address = input("파일경로를 입력해주세요 : ")
#         file_address_name = '\\ITT_student.json'
#         with open(file_address+file_address_name, encoding='utf8') as outfile:
#             json_object = json.load(outfile)
#             json_string = json.dumps(json_object)
#             json_big_data = json.loads(json_string)
#             json_Result_2 = json_big_data
#     elif file_maker == '2':
#         pass
#
# while True:
#     student_managament = input("""
# <<json기반 주소록 관리 프로그램>>
#     1. 학생 정보입력
#     2. 학생 정보조회
#     3. 학생 정보수정
#     4. 학생 정보삭제
#     5. 프로그램 종료
#     입력해주세요 : """)
#     if student_managament == '5':
#         break
#     elif student_managament == '1':
#         g_json_bigdata = {'student_ID':'ITT''{:0=3}'.format(len(g_json_bigdata)+1), # ID수정필요
#                           'student_name':input("이름은? (예:김인한) : "),
#                           'student_age': input("나이는? (예:29) : "),
#                           'address': input("주소는? (예:대전광역시 유성구 관평동 9단지 901동 302호) : "),
#                           'total_course_info':{
#                               'num_of_course_learned':input("과거수강횟수는? (예:1) : "),
#                               'learning_course_info':[
#                                     {
#                                       'course_code':input("수강코드는? (예:IB171106) : "),
#                                       'course_name':input("수강명은? (예:IOT 빅데이터 실무반) : "),
#                                       'teacher':input("강사명은? (예:이현구) : "),
#                                       'open_date':input("개강일은? (예:2017-11-06) : "),
#                                       'close_date':input("종강일은? (예:2018-09-05) : ")
#                                     }
#                                 ]
#                               }
#                           }
#         json_Result_1.append(g_json_bigdata)
#         jsonResult = json_Result_1
#
#     elif student_managament == '2':
#         student_information = input("""1.학생정보 전부출력  2.학생정보 찾기  0.이전메뉴
# 입력해주세요 : """)
#         if student_information == '0':
#             while 1:
#                 break
#         elif student_information == '1':
#             json_Result_3 = jsonResult + json_Result_2
#             for i in range(len(json_Result_3)):
#                 learning_course_info_list = json_Result_3[i]['total_course_info']['learning_course_info']
#                 print()
#                 print("＊ 학생ID : ",json_Result_3[i]['student_ID'])
#                 print("＊ 학생이름 : ",json_Result_3[i]['student_name'])
#                 print("＊ 학생나이 : ",json_Result_3[i]['student_age'])
#                 print("＊ 주소는 : ",json_Result_3[i]['address'])
#                 print("＊ 수강 정보")
#                 print("   1) 과거수강횟수 : ",json_Result_3[i]['total_course_info']['num_of_course_learned'])
#                 print("   2) 현재수강과목")
#                 print("      - 강의코드 : ",learning_course_info_list[0]['course_code'])
#                 print("      - 강의명 : ",learning_course_info_list[0]['course_name'])
#                 print("      - 강사 : ",learning_course_info_list[0]['teacher'])
#                 print("      - 개강일 : ",learning_course_info_list[0]['open_date'])
#                 print("      - 종강일 : ",learning_course_info_list[0]['close_date'])
#         elif student_information == '2':
#             student_hide = input("""
# 1.학생ID 입력
# 2. 이름 입력
# 3. 나이 입력
# 4. 주소 입력
# 5. 수강횟수
# 6. 현재수강하는 학생
# 7. 강의명
# 8. 강사
# 0. exit
#
# 입력해주세요 : """)
#             for i in range(len(json_Result_3)):
#                 if student_hide == '0':
#                     while 1:
#                         break
#                 elif student_hide == '1': # 아직 부족한 실력 및 시간 부족
#                     print(json_Result_2[i]['student_ID'])
#                     if input("ID를 입력하세요 : ") in json_Result_2[i]['student_ID']:
#                         print()
#                 elif student_hide == '2':
#                     print(json_Result_2[i]['student_name'])
#
# jsonResult += json_Result_2
# with open(file_address+file_address_name,'w',encoding='utf8') as outfile:
#     readable_result=json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
#     outfile.write(readable_result)