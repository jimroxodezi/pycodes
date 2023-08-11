
from functools import wraps
import time

__all__ = ['tracer', 'call_twice', 'timer', 
            'requires_int', 'repeat',
            'count_calls']
# decorators wrap functions around functions
# tracer is a decorator and it wraps wrapper
# around the decorated function. Using @wraps
# keeps the __name__ of the decorated function
def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Tracer entering...")
        res = func(*args, **kwargs)
        print("Tracer exiting...")
        return res
    return wrapper


def call_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("I'll call this function twice")
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed in {end - start}s")
        return res
    return wrapper

def requires_int(func):
    @wraps(func)
    def wrapper(*args):
        new_int_args = [int(arg) for arg in args]
        return func(*new_int_args)
    return wrapper

def repeat(count: int):
    def repeat_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return repeat_decorator


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # increment count attribute when wrapper is called.
        wrapper.count += 1
        return func(*args, **kwargs)
    # dynamically add count attribute to the 
    # wrapper object
    wrapper.count = 0
    return wrapper


@tracer
def hello_name(name: str):
    """function that prints hello {name} to the screen"""
    return f"Hello, {name}"


# decorators are executed in the order of closeness to 
# the inner decorated function.
# @tracer
@timer
@call_twice
def goodbye_world():
    print("Goodbye, world")


@requires_int
def add(a: int, b: int):
    return a + b

@requires_int
def subtract(a: int, b: int):
    return a - b


@repeat(10)
def print_hello():
    print("Hello")

@count_calls
def hello_count():
    print("Hello")

# goodbye_world()
# print_hello()
# print(add(1,1.0))
# hello_count()
# hello_count()
# print(hello_count.count)

# @timer
class Greeter(object):

    # @timer
    @classmethod
    def hello(cls):
        name = cls.__name__
        print(f"Hello from {name}")

    # def __call__(cls):
        # return 


if __name__ == "__main__":
    # g = Greeter()
    # g.hello()
    Greeter.hello()