def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def say_hello(name):
    return f"Hello, {name}!"

say_hello("Farhan")


from datetime import datetime
from time import sleep

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        end_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print(f"{func.__name__} returned: {result}")
        print(f"Execution time: {end_time} - {start_time}")
        return result
    return wrapper

@log_time
def say_hello(name):
    sleep(2)
    return f"Hello, {name}!"

say_hello("Farhan")