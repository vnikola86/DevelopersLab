import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# Example usage of the timer decorator
@timer
def example_function_1():
    # Some code to execute
    time.sleep(2)
    print("Function 1 executed")

@timer
def example_function_2(n):
    # Some code to execute
    time.sleep(n)
    print("Function 2 executed")

# Test the decorated functions
example_function_1()
example_function_2(3)
