while True:
    name = (input("안녕하세요 이름을 입력하세요 : "))
    while True:
        print("hi %s !! you are 1st person come here!" % name)
        break
    name = (input("안녕하세요 이름을 입력하세요 : "))
    while True:
        print("hi %s !! you are 2nd person come here!" % name)
        break
    name = (input("안녕하세요 이름을 입력하세요 : "))
    while True:
        print("hi %s !! you are 3rd person come here!" % name)
        break
    while True:
        for i in range(4,11):
            name = (input("안녕하세요 이름을 입력하세요 : "))
            print("hi %s !! you are %d th person come here!" % (name, i))
            continue
        break
    while True:
        name = (input("안녕하세요 이름을 입력하세요 : "))
        print("sorry %s, the event is closed because you are 11th person come here." % name)
        break
    break