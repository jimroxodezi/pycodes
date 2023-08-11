
"""
# working with generator functions
def gen_values():
    yield "Hello"
    yield "World"
    yield 30
    # return 42


def get_values():
    gen = gen_values()
    # print(gen)  # generator object
    print(gen.__next__())
    print(next(gen))
    print(next(gen))
    # print(next(gen))    # return value is caught in StopIteration exception

def iterate():
    for val in gen_values():
        print(val)

iterate()
get_values()

"""
from typing import Iterable

class Range(object):

    def __init__(self, __start: int, __stop: int, __step: int):
        self.start = 0 | __start
        self.stop = __stop
        self.step = __step

    def __iter__(self) -> Iterable[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += self.step



for x in Range(0, 20, 1):
    print(x)