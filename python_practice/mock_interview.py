# For example, if the input would be "John000Doe000123". 
# Then the function should return: { "first_name": "John", "last_name": "Doe", "id":
def fun(s):
    l=s.split("0")
    print(l)
    m=[]
    for i in l:
        if i.strip():
            m.append(i)
    print(m)
    n=["firstname","lastname","id"]
    j=0
    dic={}
    for k in m:
        dic.update({n[j]:k})
        j=j+1
    print(dic)

s="John000Doe000123"
fun(s)
#################################################################
from datetime import datetime
date=datetime(2024,6,24)
day=date.strftime("%A")
print(day)
#################################################################
s="John000Doe000123"
import re
su=re.sub("0"," ",s)
print(su)
fin=su.split()
print(fin)
L=["firstname","lastname","id"]
j=0
dic={}
for i in fin:
    dic.update({L[j]:i})
    j+=1
print(dic)
#################################################################
def ascii_to_hex(input_string):
    hex_values = [format(ord(char), '02x') for char in input_string]
    hex_string = ' '.join(hex_values)
    return hex_string

input_string = "hello world"
print(ascii_to_hex(input_string))
################################################################

