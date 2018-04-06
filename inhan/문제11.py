m=0
n=0
b=0
a=0
while True:
    print("게시물 건수를 입력하세요 : ")
    m=int(input())
    pass
    print("게시물 수를 입력하세요 : ")
    n=int(input())
    a = m//n
    b = m%n>0
    print("출력 :", a+b)