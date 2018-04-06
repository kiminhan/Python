sum1=0
sum2=0
sum3=0
sum=0
for a in range(1,1000):
    if a % 3 == 0:
        sum1=sum1+a
for b in range(1,1000):
    if b % 5 == 0:
        sum2=sum2+b
for c in range(1,1000):
    if c % 15 == 0:
        sum3=sum3+c
print(sum1+sum2-sum3)