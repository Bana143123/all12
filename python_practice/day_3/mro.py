# MRO is nothing but method resolution order
#Python uses the MRO to determine the order in which to look for the method.
#Example -1
class A:
    def method(self):
        return "Method in A"

class B(A):
    pass

class C(A):
    def method(self):
        return "Method in C"

class D(B, C):
    pass

d = D()
print(d.method())
#Example-2
class A:
    def method(self):
        return "Method in A"

class B(A):
    def method(self):
        return "Method in B"

class C(A):
    def method(self):
        return "Method in C"

class D(B, C):
    pass

d = D()
print(d.method())