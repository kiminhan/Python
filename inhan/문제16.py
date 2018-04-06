age=0
while True:
    age = (input("연세가 어떻게 되세요? : "))
    while True:
        if 0 < int(age) < 3:
            print("무료입니다.")
        elif 3 <= int(age) <= 12:
            print("10달러입니다. 지불해주세요.")
        elif int(age) >= 13:
            print("15달러입니다. 지불해주세요.")
        break
