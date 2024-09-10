#Appending duplicate elements to the list
lis=[1,2,3,4,5,4,3]
for i in range(len(lis)):
    if lis.count(lis[i])>1:
        lis.append(lis[i])
print(lis)
# removing duplicate elements from the list
li = [1, 2, 3, 4, 5, 4, 3]

for i in range(len(li) - 1, -1, -1):
    if li.count(li[i]) > 1:
        li.remove(li[i])
print(li)