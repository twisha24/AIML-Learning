# import seaborn as sns
# import matplotlib.pyplot as plt
# age = [20,23,25,26,21,23,29]
# sns.histplot(age)
# plt.show()

# histogram with dataframe
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df = pd.DataFrame({
#     "name":["Tina","Isha","Maya","Sneha","Naman"],
#     "age":[23,22,25,21,20],
#     "salary" :[1500,2000,5000,6000,1000]
# })
# sns.histplot(data=df,x="age",kde=True)
# plt.show()

# scatterplot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df = pd.DataFrame({
#     "age":[20,22,25,26,30],
#     "salary":[10000,15000,20000,34000,29000],
#     "gender":["Male","Female","Female","Male","Female"]
    
# })
# sns.scatterplot(data=df,x="age",y="salary",hue="gender")
# plt.show()

# countplot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.DataFrame({
#     "department":[
#         "AI" , "HR" , "IT" , "AI" , "Sales", "IT" ,"HR" , "IT" , "AI" , "HR"
#     ]
# })

# sns.countplot(data=df, x="department")
# plt.show()

# barplot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.DataFrame({
#     "department":["HR" , "IT" , "AI" , "Sales"],
#     "salary" :[1000,5000,8000,2000]
# })

# sns.barplot(data=df,x="department",y="salary")
# plt.show()

# boxplot
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.DataFrame({
#     "department" :["IT", "HR" , "AI" , "HR" , "AI" , "IT" , "HR" , "IT" , "AI"],
#     "salary":[10000,15000,30000,11000,12000,25000,17000,50000,29000]
    
# })
# sns.violinplot(data=df,x="department",y="salary")
# plt.show()

# heatmap
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.DataFrame({
#     "experience":[1,0,2,3,1],
#     "age" : [22,23,21,20,25],
#     "salary" : [1000,5000,6000,3000,4500]
# })

# correlation = df.corr()
# sns.heatmap(correlation,annot=True)
# plt.show()

# pairplot

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.DataFrame({
#     "experience":[1,0,2,3,1],
#     "age" : [22,23,21,20,25],
#     "salary" : [1000,5000,6000,3000,4500],
#     "category": [1 ,1 , 0 , 0 ,1]
# })

# correlation = df.corr()
# sns.pairplot(df,hue="category")
# plt.show()

# regplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame({
    "age" : [22,24,25,28,29],
    "salary" : [10000,15000,20000,18000,24000]
})

sns.regplot(data=df,x="age",y="salary")
plt.title("Salary Distribution")
plt.xlabel("Age")
plt.ylabel("Salary")
sns.set_theme()
plt.show()