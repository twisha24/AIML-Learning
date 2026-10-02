# colours in lineplot
# import matplotlib.pyplot as plt
# subject = ["math","phy","chem","bio"]
# marks = [23,34,56,67]
# plt.bar(subject,marks,color="red")
# plt.title("Marks Distribution")
# plt.xlabel("Subject")
# plt.ylabel("Marks")
# plt.show()
# subplots
# import matplotlib.pyplot as plt
# x = [10,20,25,40,34,56]
# y1=[12,34,56,32,16,40]
# y2 = [23,34,12,35,46,56]
# y3=[45,32,59,47,10,29]
# y4=[38,25,16,28,31,40]
# fig,axes = plt.subplots(2,2)
# axes[0,0].plot(x,y1)
# axes[0,0].set_title("Line plot")
# axes[0,1].bar(x,y2)
# axes[0,1].set_title("Bar Chart")
# axes[1,0].hist(x) 
# axes[1,0].set_title("Histogram")
# axes[1,1].scatter(x,y4)
# axes[1,1].set_title("Scatter plot")
# plt.tight_layout()
# plt.show()
# matplotlib + pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age" :[21,23,25,30,18,38],
    "salary":[10000,15000,20000,35000,29000,10000]
})
# bar chart
# plt.plot(df["age"],df["salary"])
# plt.xlabel("age")
# plt.ylabel("salary")
# plt.title("salary distribution")
# plt.show()
# histrogram
# plt.hist(df["salary"])
# plt.xlabel("salary")
# plt.ylabel("frequency")
# plt.title("salary distribution")
# plt.show()
# scatterplot
# plt.scatter(df["age"],df["salary"])
# plt.xlabel("age")
# plt.ylabel("salary")
# plt.title("salary distribution")
# plt.show()
# matplotlib and numpy
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 100)

# y = x ** 2

# plt.plot(x, y)

# plt.xlabel("X")
# plt.ylabel("X²")
# plt.title("X Squared")

# plt.show()
# saving graph 
import matplotlib.pyplot as plt
month = ["jan","feb","mar","apr"]
sales = [45,56,78,25]
plt.plot(month,sales)
plt.title("sales distribution in a year")
plt.xlabel("month")
plt.ylabel("sales")
plt.savefig("sales.png",dpi=300)
plt.show()