def sum():
    while True:
        a = input("두 수를 입력하세요 : ").split(' ')
        if a[0] == '종료':
            break
        try:
            try:
                a[0] = int(a[0])
            except:
                print("죄송합니다 첫 번째 입력이 %s입니다. 숫자를 입력하세요." % a[0])

            try:
                a[1] = int(a[1])
            except:
                print("죄송합니다 두 번째 입력이 %s입니다. 숫자를 입력하세요."% a[1])

            try:
                b = a[0]+a[1]
                c = a[0]-a[1]
                d = a[0]*a[1]
                e = a[0]/a[1]
                print(b, c, d, e)
            except:
                if a[1] == 0:
                    print("죄송합니다. 두번째 입력이 0입니다. 다른 수를 입력하세요.")
        except:
            print()
sum()

# def adder(list) :
#     result = 0
#     for x in list : result += x
#     return result

# def substractor(list) :
#     result = 0
#     for x in list : result -= x
#     return result

# def multifiler(list) :
#     result = 1
#     for x in list : result *= x
#     return result

# def divisionor(int_1, list) :
#     return int_1 / len(list)

# while 1 :
#     num_input = input("숫자 2개를 입력하십시오.(공백으로 구분, 종료 입력시 종료) : ").split(' ')
#     if num_input[0] == "종료" : break

#     for x in range(len(num_input)) :
#         try :
#             num_input[x] = int(num_input[x])
#         except ValueError :
#             print("죄송합니다. %d의 값이 [%s]입니다. 숫자를 입력하세요" %(x+1, num_input[x]))

#     print(adder(num_input))
#     print(substractor(num_input))
#     print(multifiler(num_input))
#     print(divisionor(adder(num_input),num_input))
