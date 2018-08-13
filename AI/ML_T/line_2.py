import matplotlib.pyplot as plt

# 아르바이트 일당 data sets
ys = [23000, 55000, 15000, 60000, 28000, 64000, 66000, 9000, 29000, 7000]
xs = [3, 7, 2, 8, 3, 8, 8, 1, 4, 1]

w = 0

#plt.plot(xs, ys, '+') # +로 표현
#plt.show()

# hypothesis : h(x) = w*x 1차함수
def hypothesis(x):
    global w
    return w*x

# loss(h, y) = h(x) - y
def loss(x, y):
    return hypothesis(x) - y

def cost(w):
    global xs, ys
    sum = 0
    for m, (x, y) in enumerate(zip(xs, ys)):
        sum = sum + (w*x - y)**2
    return sum / (m+1)

weights = list(range(3000, 10000))
costs = []
for weight in weights:
    c = cost (weight)
    costs.append(c)

plt.plot(weights, costs)
plt.show()

# zip 설명
#for y, x in zip(ys, xs):
#    print('sum : ', y+x)
# ys, xs를 합쳐서 y, x에 전달

# enumerate 설명
#for index, y in enumerate(ys):
#    print(str(index) + ':' , y)
#순차적 번호붙이기