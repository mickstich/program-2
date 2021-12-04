n = input("Input a string")
a=b=0
for i in n:
    if i.isdigit():
        a = a+1
    elif i.isalpha():
        b = b+1
    else:
        pass

print("Letters", b)
print("Digits", a)



