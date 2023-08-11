
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


print([*countdown(20)])

from functools import wraps

def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)
        return f
    return wrapper

# corotine decorator is for priming.
@coroutine
def finder(pattern: str):
    while True:
        input_text = yield
        if pattern in input_text:
            print("found", pattern)


jimrox_finder = finder("Jimrox")
jimrox_finder.send("Jimrox is a great programmer")
jimrox_finder.send("jijiiii")

def yielder(source):
    yield from source

def _yielder(source):
    for _ in source:
        yield _
my_countdown = countdown(20)

my_yielder = yielder(my_countdown)
print("it is time for my yielder")
for _ in range(10):
    print(next(my_yielder))

my_other_yielder = _yielder(my_countdown)
print("it is time for my other yielder")
for _ in range(10):
    print(next(my_other_yielder))
