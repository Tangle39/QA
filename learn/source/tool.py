def trans(string: str):
    """
    将字符串去掉'_',首字母大写，然后重新拼接
    :param string:
    :return: string
    """
    res = ''
    list_string = string.split('_')
    for i in list_string:
        res += i.capitalize()
    return res


def fibonacci(n):
    """
    基本的dp和生成器
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    for idx, res in enumerate(fib()):
        if idx == n-1:
            return res


if __name__ == '__main__':
    source = 'Multi-Domain Subsystem'
    print(trans(source))
    print(fibonacci(10))
