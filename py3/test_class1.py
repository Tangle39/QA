# # 实例方法
# class Kls(object):
#     def __init__(self, data):
#         self.data = data
#
#     def printd(self):
#         print(self.data)
#
#
# ik1 = Kls('leo')
# ik2 = Kls('lee')
#
# ik1.printd()
# ik2.printd()
#
#
# # 类方法
# class Kls(object):
#     num_inst = 0
#
#     def __init__(self):
#         Kls.num_inst = Kls.num_inst + 1
#
#     @classmethod
#     # 通过装饰器@classmethod的使用，方法get_no_of_instance被定义成一个类方法。
#     # 在调用类方法时，Python 会将类（class Kls）传递给cls，这样在get_no_of_instance内部就可以引用类变量num_inst。
#     def get_no_of_instance(cls):
#         return cls.num_inst
#
#
# ik1 = Kls()
# #ik2 = Kls()
#
# print(ik1.get_no_of_instance())
# print(Kls.get_no_of_instance())
class Kls(object):
    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo(%s,%s)' % (cls,x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)


ik = Kls()

# 实例方法
ik.foo(1)
print(ik.foo)
print('==========================================')

# 类方法
ik.class_foo(1)
Kls.class_foo(1)
print(ik.class_foo)
print('==========================================')

# 静态方法
ik.static_foo(1)
Kls.static_foo('hi')
print(ik.static_foo)