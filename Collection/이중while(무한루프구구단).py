a = 1
b = 1
print('[구구단 출력]')
while True:
    if a > 8:
        break
    b = 1
    a += 1
    print('-',a,'단')
    while True:
        if b > 8:
            break
        b += 1
        print(a, '*', b, '=', a * b, '입니다.')
    print('')

# a = 1
# b = 0
# print("[구구단출력]")
# while a < 10:
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