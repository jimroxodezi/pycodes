from .decorators import count_calls #import count_calls



__all__ = ['test_count_calls_0',
            'test_count_calls_3',
            'test_count_calls_with_args_and_return']



@count_calls
def no_op():
    pass


@count_calls
def same(arg):
    return arg


def test_count_calls_0():
    assert no_op.count == 0

def test_count_calls_3():
    for _ in range(3):
        no_op()
    assert no_op.count == 3

def test_count_calls_with_args_and_return():
    answer = same("hello")
    assert answer == "hello"
    assert same.count == 1

if __name__ == "__main__":
    test_count_calls_0()
    test_count_calls_3()
    test_count_calls_with_args_and_return()