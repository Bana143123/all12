#index error
my_list = [1, 2, 3]
print(my_list[5])
import abc
abc.gg()
#Overflow error
import math
math.exp(1000)
#Assertion error
assert 1==3
#zero-division error
x=5/0
print(x)
#os error
import os
os.open("xyz.txt",os.O_RDONLY)# will get OS error as we open non-existing file
#Floating-point error
raise FloatingPointError("Floating-point operation failed")
