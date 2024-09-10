#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
def checkingstr(s):
    fin = []
    mapping = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in mapping:
            fin.append(char)
        elif char in mapping.values():
            if not fin or mapping[fin.pop()] != char:
                return False
        
    
    return len(fin) == 0

print(checkingstr("narendra()"))
print(checkingstr("([narendra)"))
print(checkingstr("()"))     
print(checkingstr("()[]{}"))   
print(checkingstr("(]"))       
print(checkingstr("([)]"))     
    