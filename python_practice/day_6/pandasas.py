import pandas as pd

df=pd.read_csv("pokemon_data.csv")
print(df)
'''x=df.iloc[1:501,:11]
print(x)'''
print(df.columns)
print(df.head())
print()
print(df.tail())
print(df["Name"][:5])#getting specific column details up to how many rows we want
print(df[["Name","HP","Attack"]][:5]) #getting multiple columns up to how many rows we want

#There are 2 types of datastructures 1)series which is a 1 dimensional and 2)DataFrame is a 2 dimensional array.
series=pd.Series([1,3,2,5,6])
print("Series is :\n" ,series)
data={"A":[9,4,2,1],"B":[6,2,1,8]}
df=pd.DataFrame(data)
print(df)
#Adding new column to the dataframe
df["C"]=[5,3,2,7]
print(df)
#Adding new row to the dataframe
new_row=pd.DataFrame({"A":[5,2],"B":[7,3],"C":[7,2]})
df=pd.concat([df,new_row],ignore_index=True)
print()
print(df)
df.sort_values(by="A",inplace=True)
print(df)
df=df.sort_index()
print()
print(df)
print(df.head())
print(df.tail())
print()
print(df.info())
print()
print(df.describe())
print(df["B"])
print(df[["B","C"]])
#selecting rows by index
print(df.iloc[:4,:2])
print(df.loc[:5,"A":"C"])
#droping a column
df.drop("B",axis=1,inplace=True)
print(df)
#droping a row
df.drop(4,axis=0,inplace=True)
print(df)
df_missing = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
print(df_missing)
#dropping missing values
df_missing.dropna(inplace=True)
print(df_missing)
#filling something at Null places
df_missing1 = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3]})
df_missing1.fillna(9,inplace=True)
print(df_missing1)
print(df)
print("--------------------------------------------------------------------")
l=[["Narendra",100000,"Python","Bng"],
   ["Reddy",200000,"HR","Hyd"],
   ["Raju",300000,"Linear","Chennai"],
   ["Vyshnavi",500000,"Fire","Pune"],
   ["Rajesh",700000,"Police","Maharastra"],
   ["Pavan",900000,"Python","Bng"],
   ["Ramana",400000,"HR","Hyd"]]
df1=pd.DataFrame(l,columns=["NAME","SAL","DOMAIN","LOC"])
print(df1)
print("#############################################")
max_sal=df1.groupby(["DOMAIN","LOC"],as_index=False)["SAL"].max()
print(max_sal)