"""
when a generator function is called, a generator object is produced.
This generator object is usually in a paused state.
Generators produce data for iteration; coroutines consume data
"""

def countdown(n: int):
    print(f"counting down from {n} to 1")
    while (n > 0):
        yield n
        n -= 1
    print("Done counting down")
        
# for i in countdown(10):
#     print(i)

count = countdown(20)

# generators are iterable
# print([*countdown(20)])
# print([*x])


# coroutine
def finder(x: str):
    """
    a coroutine to find patterns
    """
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)


x = finder("python")
# priming. Can't send non-None value to a just started generator
x.send(None)
x.send("python is a programming language")

g = finder("pattern")
# another way to prime a generator
next(g)
g.send("this is a pattern")
# coroutine.close() shuts the generator object down
# this is how python garbage collects the coroutine
g.close()

def yielder(source):
    yield from source

def _yielder(source):
    for _ in source:
        yield _

y = yielder(count)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

z = _yielder(count)
# this continues from the previous state of count. Wow!!!
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))