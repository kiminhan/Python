f = open("E:\python\poll.txt", 'r')
while True:
    a = input("프로그래밍이 왜 좋으세요? : ")
    if a == "종료":
        break
    b = input("성함이 어떻게 되세요? : ")
    c = list(b)
    f = open("E:\python\poll.txt",'a')
    f.write("["+c[0]+c[1]+c[2]+"]")
    f.write(" "+a+"\n")
    print("설문에 응답해 주셔서 감사합니다.")
    break