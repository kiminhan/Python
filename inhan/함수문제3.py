f=open("E:\python\연습생.txt",'r')
d=f.read().split()

def make_world_star():
    for i in d:
        b=("신예 아이돌 %s 인기 급상승" % i)
        c=("아이돌 %s 월드스타 등극" % i)
        print(b,c,end="\n")
make_world_star()


