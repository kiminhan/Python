import numpy as np # 0보다 작은 수는 전부 0으로 나타내주는 함수

def relu(x):
    return np.maximum(0, x)