# input = "0123456789 01234 01234567890 6789012345 012322456789 1111111111"
# for ca in input.split():
#     check = [0 for i in range(10)]
#     for s in ca:
#         check[int(s)] += 1
#     print(sum(check) == 10 and all(check))

def only_one(string):
    num_set = set(string) # 중복 제거
    if len(string) == len(num_set) == 10:   # 중복 제거 한 후의 갯수와 같고 그 갯수가 10이라면
        return "true"
    else:
        return "false"

input_string = input("숫자를 입력해주세요 : ")
for s in input_string.split(" "):
    print(only_one(s), end=' ')

