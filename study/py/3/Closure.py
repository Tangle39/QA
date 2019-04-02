#相关参数和变量都保存在返回的函数中，称为“闭包（Closure）”
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,3)
'''
调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
调用函数f时，才真正计算求和的结果
'''
print(f) #<function lazy_sum.<locals>.sum at 0x10b5e81e0>
print(f())   #6
#每次调用都会返回一个新的函数
g = lazy_sum(1,2,3)
print(f==g) #False
print(f()==g())  #true