s = 'aabbbbbcccccca'

data = s[0]
count = 0

for i in s:
    if i == data[-1]:
        count = count + 1
    else:
        data = data + str(count) + i
        count = 1

result = data + str(count)

print(result)