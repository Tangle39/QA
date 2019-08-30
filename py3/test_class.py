class A(object):
    def add(self,x):
        y = x+1
        print(y)
    pass

class B(A):  #B继承
    pass

b=B()
print(isinstance(b,B)==True)    #判断一个对象是否是一个已知的类型
b.add(2)