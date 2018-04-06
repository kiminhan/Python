def ex():'''
다음 입사문제 중에서
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)
'''
help(ex) # docstring 연습

import random
# points = list({1, 3, 4, 8, 13, 17, 20})
points = list(set([random.randint(1,100) for i in range(10)])) # 이 방법은 중복있는 숫자는 제거
# points = list(set(random.sample(range(1,100),10))) 이 방법은 중복없는 숫자를 뽑는다.
points.sort()
print("수직선 위 점들은 ", points)

# 최소 거리의 점쌍을 모음
distances = [[points[0], points[1], points[1]-points[0]]]
for p1 in range(1,len(points)-1):
    left = points[p1]
    right = points[p1+1]
    distance = right - left
    if distances[0][2] > distance:
        distances = [[left, right, distance]]
    elif distances[0][2] == distance:
        distances += [[left, right, distance]]

print("가장 짧은 거리는", distances[0][2], ": ", end='')
for i in range(len(distances)):
    if i == len(distances)-1:
        print(distances[i][0],"~",distances[i][1],end='')
    else:
        print(distances[i][0],"~",distances[i][1],end=', ')