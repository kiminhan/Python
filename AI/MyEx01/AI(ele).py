# 머신러닝 수업

import numpy as np

# 1. 예측 설명
# Linear Regression
#w = 2
#x = 1

#y = w * x

#print(y)

#w1 = 2
#x1 = 1

#w2 = 4
#x2 = 2

#w3 = 6
#x3 = 3

#y = w1*x1 + w2*x2 + w3*x3
#print(y)

#W = [2, 4, 6]
#X = [1, 2, 3]
#W = np.array([2, 4, 6])
#X = np.array([1, 2, 3])

#Y = W * X # 원하는 답이 안나옴.
#Y = (W * X) * 2
#sum_Y = np.sum(Y)

#print(Y)
#print(sum_Y)

# Logistic Classification

def sigmod(y):
    y = y > 50
    return y
#
#y = sigmod(sum_Y)

#print(y)


# 동물의 종에 대한
# 포유류에 경우
W1 = np.array([2, 4, 6])
X1 = np.array([1, 2, 3])
Y1 = W1 * X1
y1 = np.sum(Y1)
#print(y1)
#print(Y1)

# 파충류의 경우
W2 = np.array([3, 5, 7])
X2 = np.array([2, 3, 4])
Y2 = W2 * X2
y2 = np.sum(Y2)
#print(y2)
#print(Y2)

# 조류의 경우
W3 = np.array([4, 6, 8])
X3 = np.array([3, 4, 5])
Y3 = W3 * X3
y3 = np.sum(Y3)
#print(y3)
#print(Y3)

# 포유류 인지 아닌지 알아내는 알고리즘
y1 = sigmod(y1)
#print(y1)

# 파충류 인지 아닌지 알아내는 알고리즘
y2 = sigmod(y2)
#print(y2)

# 조류 인지 아닌지 알아내는 알고리즘
y3 = sigmod(y3)
#print(y3)

Ws = np.array([
    [2, 4, 6],
    [3, 5, 7],
    [4, 6, 8]
])

Xs = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
])

Ys = Ws * Xs
ys = Ys.sum(axis=1)
#print(ys)
#print(Ys)

def softmax(ys):
    ys = ys > 50
    ys = ys * 1
    return ys

ys = softmax(ys)
print(ys)

def encoding_onehot(ys):
    if ys[0] == 1 and ys[1] == 0 and ys[2] == 0:
        return '포유류'
    if ys[0] == 0 and ys[1] == 1 and ys[2] == 0:
        return '파충류'
    if ys[0] == 0 and ys[1] == 0 and ys[2] == 1:
        return '조류'

y = encoding_onehot(ys)
print(y)