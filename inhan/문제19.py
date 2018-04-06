while True:
    a = input("세개의 양수를 입력하세요:").split(' ')
    if a[0] == '-1':
        print("프로그램을 종료합니다.")
        break

    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])

    if a[2] % a[0] == 0 and a[2] % a[1] == 0:
        print("%s는 %s와 %s의 공배수입니다." % (a[2], a[0], a[1]))
    else : print("%s는 %s와 %s의 공배수 아닙니다. 공부하세요." % (a[2], a[0], a[1]))
    # elif a[2] % a[0] > 0 or a[2] % a[1] > 0: 내가 짠 거는 안좋았다.
    #     print("%s는 %s와 %s의 공배수 아닙니다. 공부하세요." % (a[2], a[0], a[1]))
