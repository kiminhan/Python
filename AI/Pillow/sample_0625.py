import pandas as pd
import matplotlib.pyplot as plt
pf = pd.read_excel('http://qrc.depaul.edu/Excel_Files/presidents.xls')
print(pf)

data_frame_column_by_index = pf.iloc[:, [0]]
print(data_frame_column_by_index)


print(data_frame_column_by_index.value_counts())
#pf.value_counts().plot(kind='pie').show()

plt.plot(pd.crosstab(pf["Political Party"], pf["Years in office"]))
plt.show()