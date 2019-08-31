#能够在不修改原有业务逻辑的情况下对代码进行扩展，权限校验、用户认证、
# 日志记录、性能测试、事务处理、缓存等都是装饰器的绝佳应用场景，
# 它能够最大程度地对代码进行复用。
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#decorator就是一个返回函数的高阶函数
# def now():
#     print('15:28')
# print(now.__name__)   #函数的name属性
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
    #把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# @放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。
@log
def now():
    print('2015-3-25')
now()


def foo(num):
    return num + 1

def bar(fun):
    return fun(3)  #

value = bar(foo)  #把函数 foo 传递到 bar 中去时，foo 和 fun 两个变量名指向的都是同一个函数对象
print(value)  # 4

def outer(x):
    def inner():
        print(x)

    return inner
closure = outer(2)
closure() # 1

def outer(func):
    def inner():
        print("记录日志开始")
        func() # 业务函数
        print("记录日志结束")
    return inner

def foo():
    print("foo")

foo = outer(foo)  #没有修改 foo 函数里面的任何逻辑，只是给 foo 变量重新赋值了，指向了一个新的函数对象。
foo()


@outer
def foo2():
    print('test')
foo2()