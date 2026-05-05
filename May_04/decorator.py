#It is a function which overrides another function
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
#@decorator
def say_hello():
    print("Heloo")
say_hello()

decorated=decorator(say_hello)
decorated()