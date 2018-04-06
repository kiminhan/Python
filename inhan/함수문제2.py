q = []
i=0
while True:
    order=int(input("1. 주문, 2. 종료 \n 입력 : "))
    while True:
        if order == 1:
            a=input("안녕하세요. 원하시는 재료를 입력하세요 : ")
            if a=="종료":
                print("선택해주셔서 감사합니다.")
                print("샌드위치를 만들겠습니다.")
                for i in q:
                    print("%s 추가합니다." % i)
                print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")
                break
            q.append(a)
        elif order == 2:
            print("이용해주셔서 감사합니다.")
            break