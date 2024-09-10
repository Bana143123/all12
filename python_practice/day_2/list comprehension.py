li=[1,2,3,4,5]
out=[i*2 for i in li]
print(out)
#filtering even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#flattening nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
#using conditional statements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)
