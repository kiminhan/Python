str1 = 'Hello'
str2 = "World"
str3 = '' # empty string
str4 = ' ' # 공백문자
my_str = str1+' '+str2

str1[1:4] # 슬라이싱은 ell 까지임 1부터 4미만까지 4는 포함 x str[1],str[2],str[3]

# my_str = '"Python is easy" he said'

'"Python\'s flexibilty is good" he said'
"\"Python's flexibilty is good\" he said"
# print(str1[5])

a = "{0:^10}".format("hi") # "{:^10}".format("hi") 같다
print(a)

# student_ID = "ITT" + '{:0=3}'.format(1) # student_ID = "ITT" + '{0:0=3}'.format(1)
# print(student_ID)