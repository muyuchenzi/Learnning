# 装饰器 大概分成三个 无参数 有参数  多个装饰器
# 说是装饰器其实就是返回了一个函数，然后在返回的函数中进行对函数本体进行运行

import time


def decorator_no_args(func):
    print("decorator_no_args is running before wrapper")

    def wrapper():
        func()

    print("decorator_no_args is running after wrapper")
    return wrapper


@decorator_no_args
def foo_no_args():
    print("he")


def decoratro_args(func):
    print('里层', time.time())

    def wrapper(*args):
        res = func(*args)
        return res

    print('里层', time.time())
    return wrapper


def decorator_args_time(func):
    print('外层', time.time())
    time.sleep(3)

    def wrapper(*args):
        print(f"this is happened {time.time()}")
        res = func(*args)
        return res

    print('外层', time.time())
    return wrapper


@decorator_args_time
@decoratro_args
def foo_args(a, b, c):
    result = a + b + c
    return result


if __name__ == '__main__':
    foo_no_args()
    result = foo_args(1, 2, 3)
