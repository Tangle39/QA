# -*- coding: utf-8 -*-
#装饰器回顾19-8-16
'''ef say_hello():
    print "hello!"


def say_goodbye():
    print 'saygoodbye'+' '+"hello!"  # bug here


if __name__ == '__main__':
    say_hello()
    say_goodbye()
'''

'''
def debug():
    import inspect
    caller_name = inspect.stack()[1][3] #获取当前运行的类名函数名
    print "[DEBUG]: enter {}()".format(caller_name)

def say_hello():
    debug()
    print "hello!"

def say_goodbye():
    debug()
    print "goodbye!"

if __name__ == '__main__':
    say_hello()
    say_goodbye()
'''

def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func()
    return wrapper

#@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
@debug  #即say_hello = debug(say_hello)
def say_hello():
    print "hello!"
@debug
def say_gun():
    print "hello!"

say_hello()



say_gun()

def decorator(f):   #装饰器decorator
    def wrapper(x,y): #可调用对象
        return x+y
    return wrapper

@decorator
def func(x,y):   #被装饰对象
    return 1
print func(3,4)  # >>7