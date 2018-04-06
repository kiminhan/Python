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
                b = a[0] + a[1]
                print(b)
            except:
                print()
        except:
            print()
sum()