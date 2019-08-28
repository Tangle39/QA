import numpy as np
import string
import random
lst = [[1,3,5],[2,4,6]]
np_list = np.array(lst)
print(type(np_list))
print(np_list.shape)
print(np.zeros([2,4]))
print(np.ones([3,5]))
print(np.random.rand(2,4))
print('%.2f' %np.random.rand())
print(np.random.randint(1,10,3))
for i in range(1,10):
    print(i,end=' ')
print()
print(np.random.randn(2,2))
print(np.random.choice([10,'as',40]))   #random本身就是单独的模块
#print(''.join(np.random.sample(string.ascii_letters,5)))
print(''.join(random.sample(string.ascii_letters,5)))  #用空连接就是直接连接原来list里的元素了
print(np.arange(1,11).reshape([2,5]))