def comp_string(s):
    if not s:
        return ""
    compressed=[]
    count=1
    prev_char=s[0]
    for char in s[1:]:
        if char==prev_char:
            count+=1
        else:
            compressed.append(prev_char)
            if count>1:
                compressed.append(str(count))
            prev_char=char
            count=1
    compressed.append(prev_char)
    if count>1:
        compressed.append(str(count))
    
    return "".join(compressed)
s="dddeeettxuuedd"
out=comp_string(s)
print(out)
