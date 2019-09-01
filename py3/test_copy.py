from copy import deepcopy
import copy
# kvps = { '1' : 1, '2' : 2 }
# theCopy = kvps.copy()   #浅拷贝 a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
# kvps['1'] = 5
# print(theCopy)
# print(kvps)
# sum = kvps['1'] + theCopy['1']
# print(sum)   # 5+1
#
# ass = kvps   #赋值引用
# kvps['1'] = 3
# print(ass)
# s1 = kvps['1'] + ass['1']
#
# print(s1)  #>>5+5=10
# print(kvps)
# theCopy2 = deepcopy(kvps)  #深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
# kvps['1'] = 5
# print(theCopy2)
# print(kvps)
# s2 = kvps['1']+ theCopy2['1']
# print(s2)

a = [1, 2, 3, 4, ['a', 'b']]
b = a.copy()
c = copy.copy(a)
a[4].append('c')
a.append(5)
print('a',a);
print('b',b)
print('c',c)