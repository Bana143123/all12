import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([3,4,5])
broad=arr1+arr2
print("Broadcasting :\n",broad)
###################################
arr3=np.array([[4,3,2],[4,2,1]])
scalar=5
print(arr3*scalar)
###################################
sky=np.sum(broad,axis=0)
print("sky",sky)
sun=np.sum(broad,axis=1)
print(sun)
cn=np.sum(broad)
print(cn)
import pandas as pd
arra = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 9]])
data = {'A': [1, 3, 2], 'B': [7, 5, 6]}
df = pd.DataFrame(data)
print(df)
#indexing
ind=arra[1,2]
print(ind)
#slicing
sli=arra[0:2,1:2]
print(sli)
#pandas indexing,slicing
dat=df.at[1,"B"]
print(dat)
da=df.iloc[0:1,0:2]
print(da)
#masking
mas=arra>3
print(arra[mas])
dae=df["B"]>4
print(df[dae])
#Transposing
tran=arra.T
print(tran) #for numpy
pa=df.T
print(pa)
#Sorting
sorted=np.sort(arra,axis=0)
print("Sorting in Numpy\n",sorted)#sorting in numpy
sor=df.sort_values(by="A")
print("Sorting values in pandas\n",sor)
#Concatenating
ar1=np.array([[1,5],[3,4]])
ar2=np.array([[7,6],[9,8]])
conc=np.concatenate((ar1,ar2),axis=0)
print("Concatenation",conc)
print(conc.ndim)
print(conc.shape)
print(conc.size)
#Concatenation for pandas
df1=pd.DataFrame({"ABC":[1,2,3,4],"XYZ":[7,8,9,10]})
df2=pd.DataFrame({"ABC":[9,8,7,6],"XYZ":[8,7,6,4]})
fin=pd.concat([df1,df2],axis=0)
print(fin)
#Aggregating

agg=np.sum(arra)
print(agg)
mea=np.mean(arra)
print(mea)
#for pandas
suminpd=df.sum()
print(suminpd)
print()
meaninpd=df.mean()
print(meaninpd)
print()
#Numerical types
int_array=np.array([1,2,3,4],dtype=np.int32)
print("Integer array : ",int_array,int_array.dtype)
bool_array=np.array([True,False,True],dtype=np.bool_)
print("Boolean array type :",bool_array,bool_array.dtype)
com_array=np.array([1+2j,3+4j,8+2j],dtype=np.complex128)
print("Complex array :",com_array,com_array.dtype)
float_array = np.array([1.1, 2.2, 3.3], dtype=np.float64)
print("Float array :",float_array,float_array.dtype)
str_array=np.array(['apple', 'banana', 'cherry'], dtype=np.str_)
print("String array :",str_array,str_array.dtype)
#Structured array
dt=np.dtype([("Name",np.str_,16),("Age",np.int16),("Height",np.float16)])
structuredarray=np.array([("Reddy",24,6.0),("Narendra",23,5.9)],dtype=dt)
print(structuredarray)
print(structuredarray["Name"])
print(structuredarray["Height"])