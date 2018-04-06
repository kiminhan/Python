fticket=3
dticket=5
ticket=0
while True:
    while True:
        age=int(input("나이를 알려주세요: "))
        if age <=3:
            print("귀하는 유아이며, 무료입니다.")
        elif age >= 66:
            print ("귀하는 노인이며, 무료.")
            continue
        else:
            break
    if 4 <= age <= 13:
        print("귀하는 어린이이며, 2000원입니다.")
        money = 2000
    elif 14 <= age <= 18:
        print("귀하는 청소년이며, 3000원입니다." )
        money = 3000
    elif 19 <= age <= 65:
        print ("귀하는 성인이며, 5000원입니다.")
        money = 5000
    pay=int(input("1 : 현금, 2 : 카드 선택해주세요 : "))
    if pay==1:
        print("요금을 넣어주세요 : ")
        cash=int(input())
        if cash>money:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." %(cash-money))
        elif cash==money:
            print("감사합니다. 티켓을 발행합니다.")
        elif cash<money:
            print(money-cash,"원 부족합니다.",cash,"반환합니다.")
            continue
        ticket = ticket+1
        if ticket %7 == 0 and fticket > 0:
            fticket=fticket-1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
        elif ticket %4 == 0 and dticket > 0:
            dticket=dticket-1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
    elif pay==2:
        print("카드를 넣어주세요.")
        if age >= 60 and age <= 65:
            money=money*0.85
            print( "%d원 결제되었습니다. 티켓을 발행합니다."% (money))
        else:
            money=money*0.9
            print("%d원 결제되었습니다. 티켓을 발행합니다."% (money))
        ticket = ticket+1
        if ticket %7 == 0 and fticket > 0:
            fticket=fticket-1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
        elif ticket %4 == 0 and dticket > 0:
            dticket=dticket-1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")