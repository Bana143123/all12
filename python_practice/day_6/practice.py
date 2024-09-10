d={"A":[1,2,3],"Age":[23,24,25],"Height":[6.0,5.8,5.9]}
import pandas as pd
df=pd.DataFrame(d)
print(df)
sor=df.sort_values(by="Height")
print(sor)
import numpy as np
ar1=np.array([[1,3,4],[5,7,3],[9,4,1]])
sorp=np.sort(ar1,axis=0)
print("sorting in numpy with axis is 0 :\n",sorp)
so=np.sort(ar1,axis=1)
print("sorting in numpy axis is 1 :\n",so)
con=pd.DataFrame(ar1)
print(con)
print()
s=con.sort_values(by=2)
print(s)
print()
print(ar1.T)
print()
#masking
mas=ar1>3
print(ar1[mas])
