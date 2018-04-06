import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean(),
            'std': group.std()}

grouped = churn.custserv_calls.groupby(factor_cut)
# print(grouped.apply(get_stats).unstack())
"""
            count  max      mean  min       std
total_charges                                       
(22.86, 37.57]    70.0  5.0  1.528571  0.0  1.348337
(37.57, 52.22]   742.0  7.0  1.564690  0.0  1.305234
(52.22, 66.86]  1726.0  9.0  1.581692  0.0  1.326646
(66.86, 81.51]   735.0  9.0  1.523810  0.0  1.295209
(81.51, 96.15]    60.0  5.0  1.516667  0.0  1.359108
"""
#account _ length 열의 사분위수를 기준으로 분할한 뒤,
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
# print(grouped.apply(get_stats).unstack())
"""
                count  max      mean  min       std
account_length                                     
(0.999, 74.0]   857.0  9.0  1.506418  0.0  1.251268
(74.0, 101.0]   847.0  7.0  1.604486  0.0  1.359888
(101.0, 127.0]  803.0  8.0  1.652553  0.0  1.358479
(127.0, 243.0]  826.0  9.0  1.491525  0.0  1.286970
"""
# intl_plan 와 vmail_plan열에 대한 이진형 지시변수를 만들고,
# churn 열과 병합하여 새로운 데이터프레임을 생성하기
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
# print(churn_with_dummies.head())

"""
    churn  intl_plan_no  intl_plan_yes  vmail_plan_no  vmail_plan_yes
0  False.             1              0              0               1
1  False.             1              0              0               1
2  False.             1              0              1               0
3  False.             0              1              1               0
4  False.             0              1              1               0
"""

# total_charges를 사분위수로 분할하고, 이진형 지시변수를 만들고,
# 새로운 더미변수를 churn 데이터 프레임에 추가하기
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
# print(churn_with_dummies.head())

"""
 state  account_length  area_code     phone intl_plan vmail_plan  \
0    KS             128        415  382-4657        no        yes   
1    OH             107        415  371-7191        no        yes   
2    NJ             137        415  358-1921        no         no   
3    OH              84        408  375-9999       yes         no   
4    OK              75        415  330-6626       yes         no   

   vmail_message  day_mins  day_calls  day_charge             ...              \
0             25     265.1        110       45.07             ...               
1             26     161.6        123       27.47             ...               
2              0     243.4        114       41.38             ...               
3              0     299.4         71       50.90             ...               
4              0     166.7        113       28.34             ...               

   intl_calls  intl_charge  custserv_calls   churn  churn01  total_charges  \
0           3         2.70               1  False.      0.0          75.56   
1           3         3.70               1  False.      0.0          59.24   
2           5         3.29               0  False.      0.0          62.29   
3           7         1.78               2  False.      0.0          66.80   
4           3         2.73               3  False.      0.0          52.09   

   total_charges_1st_quartile  total_charges_2nd_quartile  \
0                           0                           0   
1                           0                           1   
2                           0                           0   
3                           0                           0   
4                           1                           0   

   total_charges_3rd_quartile  total_charges_4th_quartile  
0                           0                           1  
1                           0                           0  
2                           1                           0  
3                           0                           1  
4                           0                           0  

[5 rows x 27 columns]
"""
# 피벗 테이블 생성하기

print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], \
                        aggfunc='mean', fill_value='NaN', margins=True))

"""
                       total_charges
churn  custserv_calls               
False. 0                   58.429752
       1                   58.164391
       2                   57.534241
       3                   58.797195
       4                   64.318000
       5                   66.303077
       6                   62.150000
       7                   64.677500
       8                   64.670000
True.  0                   69.601087
       1                   70.723443
       2                   69.399080
       3                   68.931136
       4                   55.374474
       5                   52.845500
       6                   49.714286
       7                   50.578000
       8                   52.730000
       9                   70.390000
               total_charges                                              \
custserv_calls             0          1          2          3          4   
churn                                                                      
False.             58.429752  58.164391  57.534241  58.797195  64.318000   
True.              69.601087  70.723443  69.399080  68.931136  55.374474   

                                                             
custserv_calls          5          6        7      8      9  
churn                                                        
False.          66.303077  62.150000  64.6775  64.67    NaN  
True.           52.845500  49.714286  50.5780  52.73  70.39  
               total_charges                      
churn                 False.      True.        All
custserv_calls                                    
0                    58.4298  69.601087  59.904304
1                    58.1644  70.723443  59.461770
2                    57.5342  69.399080  58.894242
3                    58.7972  68.931136  59.836573
4                     64.318  55.374474  60.223373
5                    66.3031  52.845500  58.146970
6                      62.15  49.714286  54.236364
7                    64.6775  50.578000  56.844444
8                      64.67  52.730000  58.700000
9                        NaN  70.390000  70.390000
All                  58.4488  65.355963  59.449754
"""

