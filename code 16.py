import re
n= input("input your password")
x = True
while x:
    if (len(n)<6 or len(n)>12):
        break
    elif not re.search("[a-z]",n):
        break
    elif not re.search("[0-9]",n):
        break
    elif not re.search("[A-Z]",n):
        break
    elif not re.search("[$#@]",n):
        break
    elif re.search("\s",n):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Invalid Password")
