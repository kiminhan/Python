a = [-1,1,3,-2,2]
c=[]
d=[]
for b in a:
    if b<0: c.append(b)
    elif b>0: d.append(b)
print(c+d)