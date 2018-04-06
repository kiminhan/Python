c = " "
d = "*"
while True:
    print("홀수를 입력하세요.")
    a = int(input())
    if a == 0:
        print("마름모 프로그램을 종료합니다.")
        break
    elif a % 2 == 0:
        print("짝수를 입력했습니다. 다시 입력하세요.")
        continue
    elif a % 2 != 0:
        b = a
        d_count = 1
        c_count = int((b-d_count)/2)
        while True:
            print("-"*b)
            break
        while True:
            print(c*c_count,end='')
            print(d*d_count+"|")
            if d_count == b:
                break
            d_count += 2
            c_count -= 1
        b=1
        while True:
            print(c*(c_count+1),end='')
            print(d*(d_count-2))
            if d_count == b:
                break
            d_count -= 2
            c_count += 1
        while True:
            print("-"*6)
            break