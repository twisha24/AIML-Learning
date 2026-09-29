# random
# import numpy as np
# arr = np.random.rand(5)
# print(arr)

# arr = np.random.randint(1,100,7)
# print(arr)
# arr =np.random.choice([10, 20, 30, 40])
# print(arr)

# nan
# import numpy as np
# a = np.array([1,2,3,4,np.nan,6,7])
# print(np.isnan(a))
# print(np.nansum(a))
# print(np.nanmean(a))

# changing types
# import numpy as np 
# a = np.array([1,2,3,4,5])
# new_a = a.astype(str)
# print(new_a)
import numpy as np
a = np.array([
    [1, 8],
    [4, 6]
])

b = np.array([
    [3, 2],
    [1, 5]
])

print(a@b)