import time
from flask import Flask

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):

    def inner_func():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run time: {end_time - start_time}s")

    return inner_func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
