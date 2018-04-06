a = 1
b = 0
print('[구구단 출력]')
while a < 9:
    a += 1
    print('-',a,'단')
    b = 1
    while b < 10:
        print(a,'*',b,'=',a*b,'입니다.')
        b += 1
    print('')