# modifying arrays
# import numpy as np
# arr = np.array([1,2,3,4,5])
# arr[1] =200
# print(arr)

# import numpy as np
# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# arr[1,1] = 389
# print(arr)

# arithematic operation in arrys

# import numpy as np
# arr = np.array([1,2,3,4])
# arr1=arr-1
# print(arr1)

# arithematic operation between arrays

# import numpy as np
# a = np.array([10,20,30])
# b = np.array([30,40,50])
# print(a+b)


# boolean and comparison filtering 
# import numpy as np
# arr = np.array([10,20,30,40])
# print(arr[arr==30])

# statistical functions

# import numpy as np
# data = np.array([10,20,30,40,50])
# print(np.sum(data))
# print(np.min(data))
# print(np.max(data))
# print(np.std(data))
# print(np.var(data))
# print(np.mean(data))
# print(np.median(data))

# argmax and argmin
# import numpy as np
# arr = np.array([10,20,30,80,45,67])
# print(np.argmin(arr))
# print(np.argmax(arr))

# axis

# import numpy as np
# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print(np.sum(arr,axis=0))
# print(np.sum(arr,axis=1))

# reshape
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(2,3))
# print(arr.reshape(3,2))

# transpose

# import numpy as np
# arr= np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# flat = arr.flatten()
# rav = arr.ravel()
# print(flat)

# broadcasting
# import numpy as np
# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# values = np.array([10,20,30])
# print(matrix+values)
# copy vs view
# import numpy as np
# a = np.array([1,2,3,4,5])
# b= a.copy()
# b[0]=100
# print(b)
# print(a)

# import numpy as np
# a = np.array([1,2,3,4,5])
# b= a.view()
# b[0]=100
# print(b)
# print(a)

# functions
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.concatenate((a,b)))
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(np.stack((a,b)))

# where 
# import numpy as np
# a = np.array([10,15,20,45,67,89])
# arr = np.where(a>25,1,0)
# print(arr)
#  unique
# import numpy as np 
# arr = np.array([1,1,2,3,4,5,6,3,5,6])
# print(np.unique(arr))

