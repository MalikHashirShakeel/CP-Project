from time import time

def decorator(func):
    def wrapper():
        time1 = time()
        func()
        time2 = time()
        return time2 - time1
    return wrapper

@decorator
def func():
    input("Press any key: ")

print(func())


