def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

#test_var_args('yasoob', 'python', 'eggs', 'test')
# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{1} = {0}".format(key, value))
#greet_me(name = 'yasoo')   # >>yasoo = name
#greet_me(name = 'popo',sex = 1)
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

#可以使用*args或**kwargs来给这个小函数传递参数。 下面是怎样做：
args = ("two", 3, 5)
#test_args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
# 如果你想在函数里同时使用所有这三种参数， 顺序是这样的：some_func(fargs, *args, **kwargs)
