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
print(churn.head())
print(churn.describe())
"""
  state  account_length  area_code     phone intl_plan vmail_plan  \
0    KS             128        415  382-4657        no        yes   
1    OH             107        415  371-7191        no        yes   
2    NJ             137        415  358-1921        no         no   
3    OH              84        408  375-9999       yes         no   
4    OK              75        415  330-6626       yes         no   

   vmail_message  day_mins  day_calls  day_charge   ...     eve_charge  \
0             25     265.1        110       45.07   ...          16.78   
1             26     161.6        123       27.47   ...          16.62   
2              0     243.4        114       41.38   ...          10.30   
3              0     299.4         71       50.90   ...           5.26   
4              0     166.7        113       28.34   ...          12.61   

   night_mins  night_calls  night_charge  intl_mins  intl_calls  intl_charge  \
0       244.7           91         11.01       10.0           3         2.70   
1       254.4          103         11.45       13.7           3         3.70   
2       162.6          104          7.32       12.2           5         3.29   
3       196.9           89          8.86        6.6           7         1.78   
4       186.9          121          8.41       10.1           3         2.73   

   custserv_calls   churn  churn01  
0               1  False.      0.0  
1               1  False.      0.0  
2               0  False.      0.0  
3               2  False.      0.0  
4               3  False.      0.0  

[5 rows x 22 columns]
       account_length    area_code  vmail_message     day_mins    day_calls  \
count     3333.000000  3333.000000    3333.000000  3333.000000  3333.000000   
mean       101.064806   437.182418       8.099010   179.775098   100.435644   
std         39.822106    42.371290      13.688365    54.467389    20.069084   
min          1.000000   408.000000       0.000000     0.000000     0.000000   
25%         74.000000   408.000000       0.000000   143.700000    87.000000   
50%        101.000000   415.000000       0.000000   179.400000   101.000000   
75%        127.000000   510.000000      20.000000   216.400000   114.000000   
max        243.000000   510.000000      51.000000   350.800000   165.000000   

        day_charge     eve_mins    eve_calls   eve_charge   night_mins  \
count  3333.000000  3333.000000  3333.000000  3333.000000  3333.000000   
mean     30.562307   200.980348   100.114311    17.083540   200.872037   
std       9.259435    50.713844    19.922625     4.310668    50.573847   
min       0.000000     0.000000     0.000000     0.000000    23.200000   
25%      24.430000   166.600000    87.000000    14.160000   167.000000   
50%      30.500000   201.400000   100.000000    17.120000   201.200000   
75%      36.790000   235.300000   114.000000    20.000000   235.300000   
max      59.640000   363.700000   170.000000    30.910000   395.000000   

       night_calls  night_charge    intl_mins   intl_calls  intl_charge  \
count  3333.000000   3333.000000  3333.000000  3333.000000  3333.000000   
mean    100.107711      9.039325    10.237294     4.479448     2.764581   
std      19.568609      2.275873     2.791840     2.461214     0.753773   
min      33.000000      1.040000     0.000000     0.000000     0.000000   
25%      87.000000      7.520000     8.500000     3.000000     2.300000   
50%     100.000000      9.050000    10.300000     4.000000     2.780000   
75%     113.000000     10.590000    12.100000     6.000000     3.270000   
max     175.000000     17.770000    20.000000    20.000000     5.400000   

       custserv_calls      churn01  
count     3333.000000  3333.000000  
mean         1.562856     0.144914  
std          1.315491     0.352067  
min          0.000000     0.000000  
25%          1.000000     0.000000  
50%          1.000000     0.000000  
75%          2.000000     0.000000  
max          9.000000     1.000000  
"""
# 그룹별 기술통계 구하기
print(churn.groupby(['churn'])[
          ['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(
    ['count', 'mean', 'std']))

"""
       day_charge                       eve_charge                       \
            count       mean        std      count       mean       std   
churn                                                                     
False.       2850  29.780421   8.530835       2850  16.918909  4.274863   
True.         483  35.175921  11.729710        483  18.054969  4.396762   

       night_charge                     intl_charge                      \
              count      mean       std       count      mean       std   
churn                                                                     
False.         2850  9.006074  2.299768        2850  2.743404  0.751784   
True.           483  9.235528  2.121081         483  2.889545  0.754152   

       account_length                       custserv_calls                      
                count        mean       std          count      mean       std  
churn                                                                           
False.           2850  100.793684  39.88235           2850  1.449825  1.163883  
True.             483  102.664596  39.46782            483  2.229814  1.853275  
"""