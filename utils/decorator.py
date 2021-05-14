import time
from functools import wraps


def cal_time(func):
    @wraps(func)
    def calculate_time(*args, **kwargs):
        begin_time = time.time()
        callfunc = func(*args, **kwargs)
        end_time = time.time()
        print("运行时间：-> " + str(end_time - begin_time))
        return callfunc
    return calculate_time
