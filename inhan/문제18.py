def check_number(a):
    if a % 10 == 0:
        print("10의 배수입니다.")
    elif a % 10 != 0:
        print("10의 배수가 아닙니다. 멍청아")

while True:
    a = (int(input("숫자를 입력하세요 : ")))
    if a == -1:
        print("프로그램을 종료합니다.")
        break
    check_number(a)

# while True:
#     number = (int(input("양수를 입력하세요 : ")))
#     if number == -1:
#         print("프로그램을 종료합니다.")
#         break
#     while True:
#         if number % 10 == 0:
#             print ("10의 배수입니다.")
#             break
#         if number % 10 != 0:
#             print ("10의 배수가 아닙니다. 멍청아")
#             break


