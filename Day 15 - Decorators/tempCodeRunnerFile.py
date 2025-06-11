# 3. Logging Decorator
#? Create a decorator that logs the function name and its arguments before calling it.

def log_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper    

@log_function
def add(a, b):
    return a + b

add(5,10)