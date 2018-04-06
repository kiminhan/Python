while True:
    number = int(input("입력 : "))
    if number >= 1:
        print("제법인데요?")
        break
    try:
        if number <= -1:
            print("양수를 입력하세요.")
    except:
        print("양수를 입력하세요.")
    try:
        if number == 0:
            print("0은 안됩니다.")
    except:
        print("0은 안됩니다.")
