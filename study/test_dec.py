# -*- coding: utf-8 -*-
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

@debug
def say_hello():
    print "hello!"
@debug
def say_gun():
    print "hello!"

say_hello()



say_gun()