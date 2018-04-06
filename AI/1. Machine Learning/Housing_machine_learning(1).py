import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm, metrics
import random, re

housing_file_path = 'Housing.csv'
housing = pd.read_csv(housing_file_path)
# print(housing.columns)

housing['housing_driveway'] = np.where(housing['driveway'] == 'yes',1.,0.)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yes',1.,0.)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yes',1.,0.)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yes',1.,0.)
housing['housing_airco'] = np.where(housing['airco'] == 'yes',1.,0.)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yes',1.,0.)

housing_price_data = housing.price
# print(housing_price_data)

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while True:
    if i != 5: # 가격수정, 밑에 t랑 맞추거나 수정 가능하다.
        housing_price_datalist.append(housing_price_data[i])
        i = i+1
    else:
        break

housing_predictors = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'housing_driveway',\
                      'housing_recroom', 'housing_fullbase', 'housing_gashw', 'housing_airco', 'garagepl', 'housing_prefarea']

y = housing_price_data
x = housing[housing_predictors]

housing_model = DecisionTreeRegressor()
housing_model.fit(x, y)

t = 0
while True:
    if t != 15:
        # housing_price_predict_list.append(housing_model.predict(x.head())[t]) # head를 쓰게되면 5개행만 가져온다.
        housing_price_predict_list.append(housing_model.predict(x)[t])
        t = t+1
    else:
        break

# print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
result_value = 0
for value in [x - y for x, y in zip(A, B)]:
    result_value += value **2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)


# # 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
# csv = []
# with open('iris.csv', 'r', encoding='utf-8') as fp:
#     # 한 줄씩 읽어들이기
#     for line in fp:
#         line = line.strip()     # 줄바꿈 제거
#         cols = line.split(',')     # 쉼표로 자르기
#         # 문자열 데이터를 숫자로 변환하기
#         fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
#         cols = list(map(fn, cols))
#         csv.append(cols)
# # 가장 앞 줄의 헤더 제거
# del csv[0]
#
# # 데이터 셔플하기(섞기) --- (※2)
# random.shuffle(csv)
#
# # 학습 전용 데이터와 테스트 전용 데이터 분할하기 (2:1 비율) --- (※3)
# total_len = len(csv)
# train_len = int(total_len * 2 / 3)
# train_data = []
# train_label = []
# test_data = []
# test_label = []
#
# for i in range(total_len):
#     data = csv[i][0:4]
#     label = csv[i][4]
#     if i < train_len:
#         train_data.append(data)
#         train_label.append(label)
#     else:
#         test_data.append(data)
#         test_label.append(label)
#
# # 데이터를 학습시키고 예측하기 --- (※4)
# clf = svm.SVC()
# clf.fit(train_data, train_label)
# pre = clf.predict(test_data)
#
# # 정답률 구하기 --- (※5)
# ac_score = metrics.accuracy_score(test_label, pre)
#
# print("전체 데이터 수: %d" %total_len)
# print("학습 전용 데이터 수: %d" %train_len)
# print("테스트 데이터 수: %d" %(len(test_data)))
# print("정답률 =", ac_score)