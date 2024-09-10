#findall
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
y=re.findall("EX",txt) # Here no match found, So it returns empty list.
print(y)

# Search()Function.

tx = "The rain in Spain"
z = re.search("\s", tx)
print(z)
print("The first white-space character is located in position:", z.start())
print(z.string)
print(z.span())
print(z.group())
a=re.search("EX",tx) # Here no match found, So it returns None.
print(a)
#Split()Function

t = "The rain in Spain"
b = re.split("\s", t)
print(b)
#Using maxsplit parameter- it will tell how many maxsplits you want in a string.
t = "The rain in Spain"
b = re.split("\s", t, 1)
print(b)

#Sub() Function

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # Here we are using count parameter means how many replaces we want.
print(x)