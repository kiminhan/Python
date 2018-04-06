def ex():''' 
    10진수를 n진수로 변환해보자
    '''
help(ex)

import random

number_10 = random.randint(1,1000)
print(number_10,"를", end='')
number_n = int(input(" 변환할 진수는 : "))
number_warehouse = []

number = number_10
s_number = "0123456789ABCDEF"

while number:
    number_warehouse = [s_number[number % number_n]]+ number_warehouse
    number //= number_n

print(number_10,"의",number_n,"진수는", ''.join(i for i in number_warehouse),"입니다.")