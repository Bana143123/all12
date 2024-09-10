str1="Narendra"
str2="Reddy"
#string concatenation
str=str1+" "+str2
print(str)
#string repetition
rep=str1*3
print(rep)
#length of a string
print(len(str1))
#string indexing
print(str1[6])
#string slicing
print(str1[:6:1])
#string reverse
print(str1[::-1])
#Different methods in string
met="span idea "
print(met.capitalize())
print(met.title())
print(met.upper())
print(met.lower())
print(met.replace("span","Make an"))
print(met.strip())
print(met.lstrip())
print(met.rstrip())
li=met.split()
print(li)
fin="".join(li)
print(fin)
print(met.startswith("span"))
print(met.endswith("idea "))
chr="djfnc"
print(chr.isalpha())
print(chr.isalnum())
print(chr.isdigit())
print(str1.count("a"))
print(str1.find("a"))
print(str1.rfind("a"))

