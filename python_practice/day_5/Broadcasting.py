#Broadcasting allows NumPy to perform arithmetic operations on arrays of different shapes.
import numpy as np
arr1=np.array([[1,2,3],[5,6,7]])
arr2=np.array([9,1,3])
v=arr1+arr2
print(v)
print()
#NumPy Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
c=np.dot(A,B)
print(f"Matrix multiplication :\n {c}")
d=np.transpose(A)
print(f"Transpose of A is :\n{d}")
E = np.linalg.inv(A)
print("Inverse:\n", E)
#Numpy set operations
#NumPy provides functions for performing set operations on arrays, such as union, intersection, and difference.
c=np.array([1,2,3,4,5])
d=np.array([3,4,5,6,7])
un=np.union1d(c,d)
print("Union :", un)
inter=np.intersect1d(c,d)
print("Intersection :",inter)
diff=np.setdiff1d(d,c)
print("Difference :",diff)
#Numpy Vectorization
f=np.array([4,3,2,1,5,6])
print("Vector multiplication :",f*2)
print("Vecctor square root   :",np.sqrt(f))
#NumPy Boolean Indexing
#Boolean indexing allows you to filter arrays based on conditions.
s=f[f>2]
print("Boolean indexing of array f :",s)
#NumPy Fancy Indexing
#Fancy indexing involves accessing array elements using integer arrays or lists.
fancy=[1,3,5,2]
fan=f[fancy]
print("Fancy indexing :",fan)
