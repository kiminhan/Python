import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

iris = pd.read_csv('iris.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in iris.columns.str.replace(".","_")]
print(iris.columns)

# iris['iris01'] = np.where(iris['variety'] == 'Virginica',1.,0.)
iris['iris01'] = np.where(iris['variety'] == 'Versicolor',1.,0.)
# print(iris['iris01']) #1,0으로 setosa가 있으면 1 없으면 0

dependent_variable = iris['iris01']
independent_variables = iris[['sepal_length','sepal_width','petal_length','petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

sample_data_index_list = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101]
# 값의 크기가 정렬이 되지 않아도 index순서로 정렬된다.
new_observations = iris.ix[iris.index.isin(sample_data_index_list), independent_variables.columns]
# new_observations = iris.ix[iris.index.isin(random.sample(range(150),10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
# print(new_observations_with_constant) #선정된 인덱스값을 넣어주는 변수 설정

print("\n샘플링 데이터 예측 테스트")
print("10개 샘플링 데이터 리스트")
print(new_observations_with_constant.head(10))
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
index = 1
for pridicted_value in y_predicted_rounded:
    if pridicted_value > 0.75:
        # print("%d번째 샘플링 데이터 예측 결과: Virginica 확실"%index)
        print("%d번째 샘플링 데이터 예측 결과: Versicolor 확실" % index)
    elif pridicted_value > 0.5:
        print("%d번째 샘플링 데이터 예측 결과: Versicolor 애매모호" % index)
    else:
        # print("%d번째 샘플링 데이터 예측 결과: Virginica 아닌 다른 품종"%index)
        print("%d번째 샘플링 데이터 예측 결과: Versicolor 아닌 다른 품종" % index)
    index+=1