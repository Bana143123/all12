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
#Finding nth largest