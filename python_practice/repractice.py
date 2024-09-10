import re

pat=re.compile(r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9%.-]+\.[a-zA-Z]{2,}$")
def validemail(email):
    if pat.match(email):
        return True
    return False

l=["valid.email@gmail.com","@ui.co","Narendra410@gmail.com","xyz.co","valid.email@example.com"]
for email in l:
    if validemail(email):
        print(f"{email}  :is valid email")
    else:
        print(f"{email}  :is not a valid email")


#Converting number to alphabet numbers example 9876 to nineeightsevensix
def con(num):
    l={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    st=str(num)
    final=" ".join(l[di] for di in st)
    return final

n=int(input("Enter a number"))
f=con(n)
print(f"converting {n} number to letters : {f}")