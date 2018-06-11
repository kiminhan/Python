import numpy as np
import matplotlib.pyplot as plt

num_point = 1000
vectors_set = []

for i in range(num_point):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1*0.1+0.3+np.random.normal(0.0,0.033)
    vectors_set.append([x1,y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# 그래픽 표시
plt.plot(x_data, y_data, 'yx')
plt.show()