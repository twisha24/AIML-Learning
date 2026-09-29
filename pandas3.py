# import pandas as pd
# data1 = {
#     "id" :[1,2,3],
#     "name":["piya","cheenu","monu"]
# }
# student = pd.DataFrame(data1)


# data2 = {
#     "id" :[1,2,3],
#     "marks":[23,24,25]
# }
# marks = pd.DataFrame(data2)

# # result = pd.merge(student,
# #                   marks,
# #                   on="id")
# # print(result)

# result = pd.concat([student,
#                   marks],
#                   axis=1
#                   )
# print(result)
import pandas as pd
data = {
    "marks" : [21,23,45,22,11],
    "distance" : [34,45,56,78,48]
}

df= pd.DataFrame(data)
print(df.corr()) 

