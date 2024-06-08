import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


@timer_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


# contoh penggunaan
result = example_function(10000)
print('Result:', result)
