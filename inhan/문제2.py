old=0
a={1 : '유아',2 : '어린이', 3 : '청소년', 4 : '성인',5 : '노인'}
while True:
    old=int(input("나이를 알려주세요: "))
    if old <=3:
         print("귀하는",a[1],"등급에 무료입니다.")
    elif 4 <= old <= 13:
         print("귀하는",a[2],"등급에 2000원입니다.")
    elif 14 <= old <= 18:
         print("귀하는",a[3],"등급에 3000원입니다.")
    elif 19 <= old <= 65:
         print ("귀하는",a[4],"등급에 5000원입니다.")
    elif old >= 66:
         print ("귀하는",a[5],"무료.")

#old=0
#while True:
#    old=int(input("나이를 알려주세요: "))
#    if old <=3:
#         print("귀하는 유아 등급이며, 무료입니다.")
#    elif 4 <= old <= 13:
#         print("귀하는 어린이 등급이며, 2000원입니다.")
#    elif 14 <= old <= 18:
#         print("귀하는 청소년 등급이며, 3000원입니다.")
#    elif 19 <= old <= 65:
#         print ("귀하는 성인 등급이며, 5000원입니다.")
#    elif old >= 66:
#         print ("귀하는 노인 등급이며, 무료.")