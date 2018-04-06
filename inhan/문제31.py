import sys
option = sys.argv[1]

if option == '-a':
    try:
        memo = sys.argv[2]
        f = open("E:\python\memo.txt", 'r')
        f.close()
        f = open("E:\python\memo.txt", 'a')
        f.write(memo)
        f.write('\n')
        f.close()
    except FileNotFoundError as e:
        a = input("""memo.txt 파일이 없습니다. 아래 중 선택하세요. 
         1. 새로 생성하시겠습니까?
         2. 변경된 파일 경로 입력하시겠습니까?
         입력 : """)
        while True:
            if a == "1":
                f = open("E:\python\memo.txt",'a')
                memo = sys.argv[2]
                f.write(memo)
                f.write('\n')
                f.close()
                break
            elif a == "2":
                b = input("변경된 파일 경로를 입력하세요. : ")
                f = open(b,'a')
                memo = sys.argv[2]
                f.write(memo)
                f.write('\n')
                f.close()
                break

elif option == '-au':
    memo = sys.argv[2]
    memo_u = memo.upper()
    f = open("E:\python\memo.txt", 'a')
    f.write(memo_u)
    f.write('\n')
    f.close()
    print(memo_u)

elif option == '-v':
    try:
        f = open("E:\python\memo.txt", 'r')
        memo_txt = f.read()
        print(memo_txt)
        f.close()
    except FileNotFoundError as e:
        a = input("""memo.txt 파일이 없습니다. 아래 중 선택하세요. 
         1. 종료하시겠습니까?
         2. 변경된 파일 경로 입력하시겠습니까?
         입력 : """)
        while True:
            if a == "1":
                break
            elif a == "2":
                b = input("변경된 파일 경로를 입력하세요. : ")
                f = open(b,'r')
                memo_txt = f.read()
                f.close()
                print(memo_txt)
                break
