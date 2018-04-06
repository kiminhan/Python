old=0
while True:
    old=int(input("나이를 알려주세요: "))
    if old <=3:
         print("무료입니다.")
    elif 4 <= old <= 13:
         print("2000원입니다.")
    elif 14 <= old <= 18:
         print("3000원입니다.")
    elif 19 <= old <= 65:
         print ("5000원입니다.")
    elif old >= 66:
         print ("무료.")