# series
# import pandas as pd
# marks = pd.Series([80,85,88,],
#                   index = ["math" , "phy" , "chem"])
# print(marks["chem"])
# dataframe
# import pandas as pd
# data = {
#     "name" : ["tina" , "mansi" , "preeti"],
#     "age" : [23,15,30],
#     "marks" :[50,55,56],
#     "salary" : [200,56,89]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.columns)
# print(len(df))
# print(df.shape)
# print(df.loc[0:2])
# print(df.loc[1,"marks"])
# print(df.iloc[0,2])
# print(df.iloc[0:2,0:3])
# print(df["age"]>22)
# print(df[df["age"]>22])

# print(df[(df["age"]>23) | (df["marks"]>52)])

# df["avg"] = df["marks"] * 10
# df = df.drop("avg" , axis=1)
# print(df)

# df=df.drop(0)
# print(df)

# df = df.drop([0,1,2])
# print(df)
# df =df.sort_values(["salary","marks"] , ascending = [False,True])
# print(df)

import pandas as pd
import numpy as np
data = {
    "name" : ["isha" , "prita" , "prita" , "prisha" , "isha" , "ajay"],
    "age" : [28,22,22,21,28,78]
   
}

df = pd.DataFrame(data)
# df=df.isnull()
# print(df)
# df = df.isnull().sum()
# print(df)
# df = df.dropna()
# print(df)

# df["age"] = df["age"].fillna(df["age"].mean())
# print(df)
# df = df.duplicated()
# print(df)
# df = df.duplicated().sum()
# print(df)
# df = df.drop_duplicates()
# print(df)
# df = df["name"].nunique()
# print(df)
df = df["name"].value_counts()
print(df)