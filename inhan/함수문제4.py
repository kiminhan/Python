a=""
b=""
f=open("E:\python\방명록.txt",'r')
def search_visitor():
    global a
    global b
    line=f.read()
    f.close()
    a = input("이름을 입력하세요: ")
    if a in line:
        print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요." % a)
    elif a not in line:
        b=input("생년월일을 입력하세요: ")
        print("방문해 주셔서 감사합니다. 즐거운 시간되세요.")

search_visitor()

f=open("E:\python\방명록.txt",'a')
f.write(a+" "+b+"\n")
f.close()
