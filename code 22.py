def list(a):
    b=[]
    for i in (0,len(a)):
        b.append(a[0])
        b.append(a[len(a)-1])
        return b

a=[15,2,3,3,4,5,6,7,8,999]
print(list(a))
