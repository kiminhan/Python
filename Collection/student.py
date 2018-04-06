import json

student_result = []
student_information = []

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
        try:
            with open('ITT_Student.json','r',encoding='utf8') as outfile:
                student_information = [
                    {
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
                ]
        except :
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')

        with open('ITT_Student.json', 'a') as outfile:
            student_result.append(student_information)
            outfile.write(student_result)

        # # student.append(student_information)
        # # student_ID = student_information[0].get('student_ID')
        # name = student_information[0].get('name')
        # age = student_information[0].get('age')
        # address = student_information[0].get('address')
        # lecture_information = student_information[0].get('lecture_information')
        # past_lecture_subject = student_information[0].get('lecture_information').get('past_lecture_subject')
        # recent_lecture_subject = student_information[0].get('lecture_information').get('recent_lecture_subject')

# student_ID = str(student_ID)
# name = str(name)
# age = str(age)
# address = str(address)
# past_lecture_subject = str(past_lecture_subject)
# recent_lecture_subject = str(recent_lecture_subject)
#
#
# print(student_result)

# with open('ITT_Student.json','w',encoding='utf8') as outfile:
#     readable_result=json.dumps(student_result,indent=4,sort_keys=True,ensure_ascii=False)
#     outfile.write(readable_result)
#     print('ITT_Student.json SAVED')
