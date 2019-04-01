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
@log    #把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
def now():
    print('2015-3-25')
now()