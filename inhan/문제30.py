def getTotalPage(m,n):
    if m % n == 0 and m / n > 0:
        return m // n
    elif m % n != 0 and m / n > 0:
        return m // n +1

f = open("E:\python\condition.txt",'r')
line_list = f.readlines()
f.close()

for i in line_list:
    try:
        result=i.split()
        m = int(result[0])
        n = int(result[1])
        print("게시물 총 건수: %s, 한페이지에 보여줄 게시물 수 : %s, 총 페이지 수: %s" % (m, n, getTotalPage(m, n)))
    except:
        continue
