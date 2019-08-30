class Person:
    def __init__(self):
        pass
    def getAge(self):
        print(__name__)
p = Person()
p.getAge()
#当前程序运行在这个模块中，__name__ 的名称就是__main__