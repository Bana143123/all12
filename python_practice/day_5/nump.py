#Numpy array creation
import numpy as np
oned_arr=np.array([1,2,3,4,5])
print(f"one dimensional array : {oned_arr}")
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Two dimensional array : {array_2d}")
array_3d= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(f"Three dimensional array : {array_3d}")
#Numpy datatypes : we can find datatype using dtype
oned_arr=np.array([1,2,3,4,5],dtype=float)
print(f"one dimensional array : {oned_arr}")
print("Datatype",oned_arr.dtype)
#Numpy array attributes
#1)shape,Number of dimensions,data type,size of array
ar=np.array([[7,8,9,10],[9,5,4,6]])
#ar=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("shape",ar.shape)
print("Number of dimensions",ar.ndim)
print("Size of the array",ar.size)
print("Data type",ar.dtype)
#saving an array to the specific file
np.save("han.txt.npy",ar)
#Loading an array from the file
loaded=np.load("han.txt.npy")
print("Loaded array:\n",loaded)
#Numpy array indexing
ar=np.array([[7,8,9,10],[9,5,4,6]])
print(ar[0][3])
print(ar[-1][0])
#Numpy array slicing
array = np.array([10, 20, 30, 40, 50,6])

print("Elements from index 1 to 3:", array[1:4])

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Subarray:\n", array_2d[0:2, 1:3])
#reshaping 1d array to 2d array
sh=array.reshape((2,3))
print("Reshaped array:\n",sh)
#changing reshaped array to flattened array
flat=sh.flatten()
print("Flattened array:\n",flat)
#Numpy array operations
arr1=np.array([3,4,6])
arr2=np.array([5,4,2])
print("Addition of two numpy arrays:\n",arr1+arr2)
print("Multiplication of two numpy arrays:\n",arr1*arr2)
#Numpy Arithmetic array operations
sub=arr1-5
print("Subtraction of arr1 is :\n",sub)
div=arr1//3
print("Division of arr1 is:\n",div)
#Numpy array Functions
su=np.sum(arr1)
print("Sum :",su)
mea=np.mean(arr1)
print("Mean :",mea)
mid=np.median(arr1)
print("Median : ",mid)
#Numpy Math Functions
ma=np.array([10, 20, 30, 40, 50,6])
square_root=np.sqrt(ma)
print("Square root of given array ma :\n",square_root)
expo=np.exp(ma)
print("Exponential of given array ma :\n",expo)
#Numpy statistical functions
array = np.array([1, 2, 3, 4, 5])
std_result = np.std(array)
print("Standard Deviation:", std_result)
var_result = np.var(array)
print("Variance:", var_result)
#Numpy String Functions
string_array = np.array(['numpy', 'is', 'awesome'])
cap=np.char.capitalize(string_array)
print("Capitalize of each strring :\n",cap)
tit=np.char.title(string_array)
print("Title of each strring :\n",tit)
added_string = np.char.add(string_array, '@')
print("Added String:", added_string)
#Numpy comparison\Logical Opertions
array1 = np.array([1, 2, 3])
array2 = np.array([3, 2, 1])
comp_result = array1 == array2 #it's comparing element wise in each array
print("Comparison:", comp_result)
and_result = np.logical_and(array1 < 3, array2 < 3)
print("Logical AND:", and_result)
or_result = np.logical_or(array1 < 3, array2 < 3)
print("Logical OR:", or_result)