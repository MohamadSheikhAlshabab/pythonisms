from functools import wraps
import time

def spent(func):
    @wraps(func)
    def wrapper_spent(*args,**kwargs):
        t0 =time.time()
        old_value = func(*args,**kwargs)
        t1 = time.time() - t0
        time_spent = t1-t0
        return time_spent
    return wrapper_spent
        

def slow_down(func):
    @wraps(func)
    def wrapper_slowdown(*args,**kwargs):
        time.sleep(2)
        old_value = func(*args,**kwargs)
        return old_value
    return wrapper_slowdown
