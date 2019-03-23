pre = [1,2,4,7,3,5,6,8]
index = pre.pop(0)
print index
print pre
tin = [4,7,2,1,5,3,8,6]
b = tin.index(index)
print b
print tin[b+1:]
print tin[:b]