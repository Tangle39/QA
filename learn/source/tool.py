import random


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
        if idx == n - 1:
            return res


def primes(n):
    """
    Generate all prime numbers up to n.
    The code is from chatGPT
    <埃拉托色尼筛法>
    这个实现使用了一个布尔类型的sieve列表来存储是否为素数。开始时，我们将sieve列表的前两个元素标记为False，即0和1不是素数。然后，我们从2开始，逐个将素数的倍数标记为False，
    直到达到sqrt(n)为止。最后，我们迭代sieve列表中所有为True的元素，生成素数序列。和之前的斐波那契数列的例子一样，这个函数同样使用生成器，以便在需要时按需生成下一个素数。
    这个实现可以很好地处理大范围内的素数，并且具有很好的时间和空间复杂度。
    如果你需要获取所有的素数列表，可以将生成器转换成一个列表，方法是在函数调用时使用list()函数，例如：
    prime_list = list(primes(1000))
    """
    if n <= 1:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False
    for i in range(2, n + 1):
        if sieve[i]:
            yield i


def random_sum():
    """
    随机生成128个正整数，每个数小于1024，总和为8192
    """
    nums = [0] * 128
    target_sum = 8192
    rand_nums = [random.randint(1, 1024) for _ in range(128)]
    rand_sum = sum(rand_nums)
    # 初次分配，使得sum接近target
    for i in range(128):
        nums[i] = rand_nums[i] * target_sum // rand_sum

    diff = target_sum - sum(nums)
    while diff > 0:  # 如果有剩余，则将剩余的值加到nums中
        idx = random.randint(0, 127)
        if nums[idx] < 1024:
            nums[idx] += 1
            diff -= 1
    return nums


if __name__ == '__main__':
    res = random_sum()
    print(res, len(res), sum(res))
