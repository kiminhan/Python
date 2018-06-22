import numpy as np # 시그모이드 함수란 어떤 수가 오더라도 0과 1사이에 수가 오게 만든다.

def sigmoid(x):
    return 1 / (1+np.exp(-x))

x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])

print(w1.shape)
print(x.shape)
print(b1.shape)

a1 = np.dot(x, w1) + b1

z1 = sigmoid(a1)

print(a1)
print(z1)

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

print(z1.shape)
print(w1.shape)
print(b2.shape)

a2 = np.dot(z1, w2) + b2
z2 = sigmoid(a2)
