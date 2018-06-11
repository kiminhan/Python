import pandas as pd

tbl = pd.DataFrame([["A","B","C",1,2],["D","E","F",3,4],["G","H","I",5,6],["J","K","L",7,8],["M","N","O",9,10]])

print(tbl)
print("------------------")
print(tbl.T)