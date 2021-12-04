def list(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y
a = [88,2,66,4,33,2,11,88,4]
print (list(a))
