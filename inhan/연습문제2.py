number = input("숫자를 입력하세요: ")


def check():
    a = []
    for i in number:
        a.append(int(i))
    if sorted(a) == list(range(0,10)):
        print("True")
    else:
        print("False")
