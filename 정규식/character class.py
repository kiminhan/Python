import re
# 대문자 소문자 구분해야된다.
# p = re.compile('[abc]') # 문자열중에 첫번째 문자가 'a,b,c'랑 매칭이 되느냐
# m = p.match("ability")
# m = p.match("zebra") # 매칭이 안됨
# print(m)

# [a][b] 같은 경우에는 문자열중에 첫번째 문자가 a 두번째 문자가 b가 와야지 매칭이 된다.

# p = re.compile('[e][l][e]')
# p = re.compile('e') # 가능
# p = re.compile('ela') # 불가능
# p = re.compile('[ela]') # 가능
# m = p.match("element")
# print(m)

# p = re.compile('a[abc]c') # 불가능
# m = p.match("aabc")
# p = re.compile('a[abc]c') # 가능
# m = p.match("acc")
# print(m)

# p = re.compile('[a-z]') # 가능 [abcdefghijklmnopqrstuvwxyz] 같은 의미
# m = p.match("a!") # [abcdefghijklmnopqrstuvwxyz] 같은 의미이나 이렇게 하면 매칭은 안됨, [a-z] 가능
# print(m)

# p = re.compile('[a-z,A-Z]')
# m = p.match(",") # 가능
# print(m)
#
# p = re.compile('[a-zA-Z]')
# m = p.match("z") # 가능
# print(m)

# ^ caret의 의미

# p = re.compile('[^a-zA-Z]')
# m = p.match("z") # 불가능
# print(m)
# p = re.compile('[^0]')
# m = p.match("1") # 가능
# print(m)
# p = re.compile('[^\d]')
# m = p.match("k") # 가능
# print(m)

# p = re.compile('[\s]') # 공백문자에 매치
# # m = p.match(" ") # 가능
# m = p.match("") # 불가능
# print(m)
#
# p = re.compile('[\S]') # 공백문자가 아닌것에 매치
# m = p.match(" ") # 불가능
# m = p.match("a") # 가능
# print(m)

# p = re.compile('[\w]') # 문자+숫자에 매치
# m = p.match("1") # 가능
# # m = p.match("*") # 불가능
# print(m)
#
# p = re.compile('[\W]') # 문자+숫자가 아닌것에 매치
# # m = p.match("1") # 불가능
# m = p.match("*") # 가능
# print(m)

# p = re.compile('a.b') # dot(.) 은 a와 b사이에 줄바꿈문자를 제외한 어떤 문자가 들어가도 모두 매치
# m = p.match("ab") # 불가능
# m = p.match("a*b") # 가능
# print(m)

# p = re.compile('a*b') # a가 0번이상 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('a+b') # a가 1번이상 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('a{0,5}b') # 0에서 5번 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('ab?c') # b가 0~1번 사용되면 매치
# m = p.match("ac") # 가능
# m = p.match("abbc") # 불가능
# print(m)

# p = re.compile('[a-z]+') #
# m = p.match("3 python") # 불가능
# m = p.search("3 python") # 가능
# m = p.findall("pythons python!") # 컴파일안에 있는 것들만 리턴
# m = p.finditer("pythons python") # findall과 동일하지만 그 결과로 반복 가능한 객체를 리턴
# print(m)

# p = re.compile("^python\s\w+",re.MULTILINE) # MULTILINE을 쓰게되면 모든 데이타에서 python이 들어간 것을 찾아준다.
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))

# p = re.compile(r"(\b\w+)\s+\1")
# m = p.search("Paris in the the spring").group()
# print(m)

# p = re.compile(r"(\w+)\s\1") # 백슬러시를 하기위해 r을 넣어줘서 구분해줘야한다.
# m = p.search("sdf Hello Hello").group()
# print(m)

# p = re.compile(r"(\w+)\s(\w+)\s\1\s\2") # \2 2번쨰 그룹 참조
# m = p.search("sdf Hello World Hello World Hello dkfjksdk").group()
# print(m)
#
# p = re.compile(r"(\w+)\s(\w+)\s\2\s\1")
# m = p.search("sdf Hello World World Hello dkfjksdk").group()
# print(m)

# print("첫번째 그룹 이름 활용") (그룹네이밍)
# p = re.compile(r"(?P<greeting>\w+)\s\1")
# m = p.search("sdf Hello Hello ")
# print(m.group("greeting"))

# print("\n두번째 그룹 이름 활용")
# p = re.compile(r"(?P<greeting>\w+)\s(?P<destination>\w+)\s\1\s\2")
# m = p.search("sdf Hello World Hello World dfskdfsk ")
# print(m.group("greeting"))
# print(m.group("destination"))
# print(m.group("destination")) # 그룹이름으로 매칭된 단어를 가져올 수 있다.

# p = re.compile(".+:") # :이 나온다 # http: 까지 나온다. (전방탐색)
# m = p.search("http://google.com")
# print(m.group())
#
# p = re.compile(".+(?=:)") # : 는 소모되지 않는다. # http까지만 나온다. (긍정형 전방 탐색)
# m = p.search("http://google.com")
# print(m.group())

def check_match(p,file_name):
    m = p.match(file_name)
    if m:
        print(m)

# Step1] 파일명.확장자를 나타내는 정규식
file_name_candidates=["foo.bar","autoexec.bat","sendmail.cf"]

p = re.compile(".*[.].*$")

print("첫번째 정규식 테스트: .*[.].*$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step2] 확장자가 bat 파일 제외
p = re.compile(".*[.][^b].*$")
print("\n두번째 정규식 테스트: .*[.][^b].*$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step3] 확장자가 bat 파일 제외 두번쨰 시도
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$") # or(|)가 들어갔긴 때문에 [^b]. 만 해주면 bat만 제외한 것을 나오게할 수 있다.
print("\n세번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t]$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step4] 확장자가 bat 파일 제외 세번쨰 시도
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$") # ?는 .(0~1번 반복가능하게) .에 아무것도 안들어가도 가능하게
print("\n네번째 정규식 테스트: .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
for file_name in file_name_candidates:
    check_match(p,file_name)

p = re.compile(".*[.](?!bat$).*") # (부정형 전방탐색)
print("\n부정형전방탐색 테스트: .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
for file_name in file_name_candidates:
    check_match(p,file_name)
