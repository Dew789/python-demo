import time
import functools

def calculate_run_time(max_time=5):
    """If run_time greater than max_time, print function name"""
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper2(*args, **kwargs):
            currnet = time.time()
            func(*args, **kwargs)
            now = time.time()
            if (int(now-currnet) > max_time):
                print(func.__name__)
        return wrapper2

    return wrapper1
