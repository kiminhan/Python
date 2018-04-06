try:
    f = open("E:\python\poll.txt", 'r')
    f.close()
except FileNotFoundError as e:
    a = input("""poll.txt 파일이 없습니다. 아래 중 선택하세요. 
     1. 종료
     2. 변경된 파일 경로 입력
     입력 : """)

    while True:
        if a == "1":
            break
        elif a == "2":
            b = input("변경된 파일 경로를 입력하세요. : ")
            f = open(b,'a')
            while True:
                a = input("프로그래밍이 왜 좋으세요? : ")
                if a == "1":
                    break
                b = input("성함이 어떻게 되세요? : ")
                c = list(b)
                f.write("[" + c[0] + c[1] + c[2] + "]")
                f.write(" " + a + "\n")
                print("설문에 응답해 주셔서 감사합니다.")
                continue
