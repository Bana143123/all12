import numpy as np
arr1=np.array([[1,2,3],[5,6,7]])
arr2=np.array([[4,3,2],[4,3,2]])
c=np.concatenate((arr1,arr2),axis=0)
print(c)
mid=np.median(c)
print(mid)