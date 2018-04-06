# while 구조
# while 다음엔 조건문 ex) while 조건문:, while a < 9

# a = 1
# b = 0
# print("[구구단출력]")
# while True:
#     a += 1
#     if b == 9:
#         b = 0
#     if a == 10:
#         break
#     print("-", a, '단')
#     while b < 9:
#         b += 1
#         print(a,'*',b,'=',a*b,'입니다.')
#     print("")

i = 0
while True:
    i += 1
    if i >= 6: break
    print(i*'*')