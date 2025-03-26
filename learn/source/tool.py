import multiprocessing as mp
import random
import threading
import time
from multiprocessing import Pool

mp.set_start_method('fork')
import atexit


def unique_random_numbers():
    # 随机不重复数
    generated_numbers = list(range(100000))  # 创建一个包含0到99999的列表
    random.shuffle(generated_numbers)  # 打乱列表中的元素顺序
    while generated_numbers:
        yield generated_numbers.pop()


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


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def example_function(n):
    time.sleep(n)
    return f"Function ran for {n} seconds"


@timing_decorator
def cal_large_sum(arr):
    def compute_sum(_arr, result, idx):
        time.sleep(5)
        # print(f'start {_arr[0]} end {_arr[-1]}')
        result[idx] = sum(_arr)

    n_threads = 4
    chunk_size = len(arr) // n_threads
    threads = []
    results = [0] * n_threads

    for i in range(n_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        thread = threading.Thread(target=compute_sum, args=(arr[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return sum(results)


def compute_partial_sum(chunk):
    return sum(chunk)


@timing_decorator
def cal_sum_2(arr):
    n_processes = 4
    chunk_size = len(arr) // n_processes

    # 分割数组为多个子任务
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(n_processes)]

    with Pool(n_processes) as pool:
        results = pool.map(compute_partial_sum, chunks)
    return sum(results)


@timing_decorator
def cal_sum(arr):
    return sum(arr)

class Test:
    def clean_up(self):
        print("Cleaning up resources...")

test = Test()
atexit.register(test.clean_up)
if __name__ == '__main__':
    cnt = 0
    while True:
        print('sleep')
        time.sleep(1)
        cnt += 1
        if cnt == 5:
            break
