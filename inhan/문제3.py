old=0
money=0
while True:
    old=int(input("나이를 알려주세요: "))
    if old <=3:
         print("귀하는 유아 등급이며, 무료입니다.")
    elif 4 <= old <= 13:
        print("귀하는 어린이 등급이며, 2000원입니다.")
        money = int(input("요금을 넣어주세요: "))
        if money == 2000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 2000:
             print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-2000))
        elif money < 2000:
            print(2000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
    elif 14 <= old <= 18:
        print("귀하는 청소년 등급이며, 3000원입니다.")
        money = int(input("요금을 넣어주세요: "))
        if money == 3000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 3000:
             print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-3000))
        elif money < 3000:
            print(3000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
    elif 19 <= old <= 65:
        print ("귀하는 성인 등급이며, 5000원입니다.")
        money = int(input("요금을 넣어주세요: "))
        if money == 5000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 5000:
             print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-5000))
        elif money < 5000:
            print(5000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
    elif old >= 66:
         print ("귀하는 노인 등급이며, 무료.")