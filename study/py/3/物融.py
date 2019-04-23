def foo(default=[]):
    default.append(4)
    return default


d = []

default = []
foo(default)
foo(default)

print(default)  # [4,4]因为default有值，所以不是默认的[]

print(foo(d))  # [4]


