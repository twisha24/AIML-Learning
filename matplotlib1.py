# line plot
# import matplotlib.pyplot as plt
# x =[1,2,3,4,5,6]
# y=[10,12,23,15,21,11]
# plt.plot()
# plt.show()
# x axis and y axis
# import matplotlib.pyplot as plt
# months = ["jan","feb","march","april","may"]
# days=[11,23,34,22,55]
# plt.plot(months,days)
# plt.show()
# label markers
# import matplotlib.pyplot as plt
# months = ["jan","feb","march","april","may"]
# sales=[11,23,34,22,55]
# plt.title("sales over months")
# plt.xlabel("months")
# plt.ylabel("sales")
# plt.plot(months,sales,linestyle="-",marker="o")

# plt.show()
# grid
# import matplotlib.pyplot as plt
# months = ["jan","feb","may","june"]
# sales =[75,80,65,87]
# plt.title("months vs sales")
# plt.xlabel("months")
# plt.ylabel("sales")
# plt.plot(months,sales)
# plt.grid()
# plt.show()

# bar chart
# import matplotlib.pyplot as plt
# subject = ["phy","chem","math","eng","bio"]
# marks = [55,60,45,67,70]
# plt.title("subject and marks")
# plt.xlabel("subject")
# plt.ylabel("marks")
# plt.barh(subject,marks)
# plt.show()

# import matplotlib.pyplot as plt
# ages = [18, 19, 20, 20, 21, 21, 21, 22, 23, 24, 25, 25, 26]
# plt.hist(ages)

# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")

# plt.show()
# import matplotlib.pyplot as plt
# salary = [10000,20000,23000,56000,70000,450000,56000,12000,34000]
# plt.hist(salary,bins=3)
# plt.title("salary distribution")
# plt.xlabel("salary")
# plt.ylabel("frequency")
# plt.show()

# scatter plot
import matplotlib.pyplot as plt
hours = [1,2,3,2,4,5]
marks = [20,21,23,12,18,25]
plt.scatter(hours,marks)
plt.title("Marks distribution according to hours")
plt.xlabel("hours")
plt.ylabel("marks")
plt.show()



























