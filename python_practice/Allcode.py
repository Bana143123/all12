'''s="ddd123@#r8*"
digits=""
letters=""
special=""
for i in s:
    if i.isdigit():
        digits+=i
    elif i.isalpha():
        letters+=i
    else:
        special+=i
final="".join(digits),"".join(letters),"".join(special)
print(final)'''
'''s="r tff u"
out=s.replace(" ","9")
print(out)'''
l=[[1,2,3],[5,6,7]]
ou=[i for j in l for i in j]
print(ou)
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)
o=[1,[2,3],[4,5]]
flat=[]
for i in o:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)
o=[1,[2,3],[4,5]]
fin=[]
[fin.extend(i) if isinstance(i,list) else fin.append(i) for i in o]
print(fin)
f="Narendra"
sh=""
for i in f:
    sh=i+sh
print(sh)
#Counting each character occurance in string
f="Narendra"
d=[]
uni=set()
for i in f:
    if i not in uni:
        d.append((i,f.count(i)))
        uni.add(i)
print(d)
from collections import Counter
r=Counter(f)
print(r)
p=[1,3,4,5,6,5,3]
#p=['Narendra', 'Kumar', 'Reddy', 'Bana']
left=0
right=len(p)-1
while left<right:
    p[left],p[right]=p[right],p[left]
    left+=1
    right-=1
print(p)
for i in p:
    if p.count(i)>1:
        p.remove(i)
print(p)
def pat(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1, 0,-1):
            print(j,end=" ")
        print()
pat(5)
print("###################################")
def tri(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))
tri(5)
my_li=[12,15,76,"a","b",45]
digit=0
for i in my_li:
    if isinstance(i,int):
        digit+=i
print(digit)
print("&&&&&")
sum=0
for i in my_li:
    if isinstance(i,int):
        for j in str(i):
            sum+=int(j)
print(sum)
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fi=fib()
for _ in range(10):
    print(next(fi))
print("Another way for fibnocci")
def fibn(n):
    f=[0,1]
    for i in range(2,n):
        y=f[-1]+f[-2]
        f.append(y)
    return f
u=fibn(10)
print(u)
'''print("Prime numbers")
def pri(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if pri(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")'''
print("Reversing a words")
v="Narendra Kumar Reddy Bana"
d=v.split()
print(d)
re=[]
for i in range(len(d)):
    re.append(d[-i-1])
print(re)
q=" ".join(re)
print(q)
l=[2,4,6,8,4,1,45]
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
#sum of contiguous subaray
def max_num(nums):
    max_start = nums[0]
    max_end = nums[0]
    
    for i in range(1, len(nums)):
        max_end = max(nums[i], max_end + nums[i])
        max_start = max(max_start, max_end)
    
    return max_start

# Example usage:
outnuts = [-2, 1, -3, 4, -1, 2, -5, 4, 10]
print("The maximum sum of the contiguous subarray is:", max_num(outnuts))

#Finding nth largest number
def larg(n):
    l=[1,2,3,4,45,3,90]
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
    x=l[n-1]
    l.remove(n-1)
    print(f"The largest number : {x}")
    return l
n=4
final=larg(n)
print(final)

#fibnocci series
def fib(n):
    if n<=1:
        return 1
    fi=[0,1]
    for i in range(2,n+1):
        y=fi[-1]+fi[-2]
        fi.append(y)
    return fi
finalre=fib(10)
print(finalre)

#fibnocci using recursive
def fibre(m):
    if m<=1:
        return m
    return fibre(m-1)+fibre(m-2)
def generate_fib_sequence(m):
    return [fibre(i) for i in range(m+1)]

w=generate_fib_sequence(10)
print(w)


