while True:
    number = input("숫자를 입력하세요(-1:종료, all:구구단전체출력) : ")
    if number == "-1":
        break

    while True:
        if number == "all":
            for i in range(2,10):
                for j in range(1,10):
                    print("%d * %d = %d" % (i,j,i*j))
            break
        try:
            if int(number) < -1:
                raise ValueError
        except ValueError:
            print("양수를 입력하세요.")
            break
        else:
            for i in range(1,10):
                a = int(number) * int(i)
                print("%d * %d = %d" % (int(number), int(i), a))
        break