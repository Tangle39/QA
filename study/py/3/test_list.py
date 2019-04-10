#+= 和append的区别
res = []
res.append([1,2])
res.append([3,4])
print(res)
b= []
b+= [2,3]
b+= [1,2]
print(b)
b += {'a':1,'b':2}

print(b)
