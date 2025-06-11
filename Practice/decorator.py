# # 3. Logging Decorator
# #? Create a decorator that logs the function name and its arguments before calling it.

# def log_function(func):
#     def wrapper(*args, **kwargs):
#         result = args        
#         print(f"arguments are: {result[0]} and {result[1]} ")        
#         Added =  func(*args, **kwargs)        
#         return Added

#     return wrapper    

# @log_function
# def add(a, b):
#     return a + b

# print("arguments are",add(5,10))



# # 4. Execution Timer
# #? Write a decorator that measures how long a function takes to run.


# import time

# def timer(fun):
#     def wrapper(*args, **kwargs):

#         timeS = time.time()

#         fun(*args, **kwargs)

#         timeE = time.time()
#         result = (timeE - timeS) 
#         print(result)
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(2)
#     print("Done")
# slow_function()