

from metaprogramming.decorators import timer
# from metaprogramming import test_count_calls_with_args_and_return
import metaprogramming


@timer
def print_hello():
    print("Hello")




print_hello()
metaprogramming.decorators_test.test_count_calls_with_args_and_return()
# print(dir(metaprogramming))

# metaprogramming