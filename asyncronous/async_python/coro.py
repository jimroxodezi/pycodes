
"""
async keyword is a new way of creating (native) coroutines in python
since python 3.5. async.coroutine decorator have been deprecated
in favour of async/await syntax
"""


def greet(name):
    return 'Hello ' + name

async def _greet(name):
    return "Hello, " + name

# print(greet("Jimrox"))    # runs like a normal function
# print(_greet("Jimrox"))   # returns a coroutine object

g = _greet("Something for a little demonstration")
# print(g)
# g.send(None)    #raises StopIteration
# g.send("Jimrox is a great programmer")    # won't work. Needs a None value


def run(coroutine):
    """
    This run function acts like an event loop; runs coroutines.
    """
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
    


print(run(_greet("Jimrox")))
print(run(g))


async def main():
    print(await _greet("Odezi"))

run(main())

async def myMain():
    names = ["Jimrox", "Odezi", "Favour", "Emeria"]
    for name in names:
        print(await _greet(name))

# run(myMain())


async def fib(n: int):
    if n < 2:
        return 1
    else:
        return await fib(n - 1) + await fib(n - 2)
    

async def fibmain():
    for i in range(30):
        print(await fib(i))

# run(fibmain())


async def okay():
    f = await fib(10)
    d = {}
    d[await fib(6)] = await fib(2)
    x = await fib(3) - await fib(1)
    print(f, d, x)

run(okay())