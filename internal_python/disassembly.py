

import dis
# import ast


# def _adder(a: int, b: int):
#     return a + b

def adder(a: int, b: int) -> int:
    # return _adder(a,b)
    return a + b

dis.dis(adder)

# # print(adder.__code__.co_argcount)
# print(list(adder.__code__.co_code))

# # for c in list(adder.__code__.co_code):
# #     print(chr(c))

# print(adder.__code__.co_filename)
# print(adder.__code__.co_flags)
# print(adder.__code__.co_firstlineno)
# print(adder.__code__.co_varnames)
# print(adder.__code__.co_kwonlyargcount)
# # print(adder.__code__.co_lnotab)
# print(adder.__code__.co_name)
# print(adder.__code__.co_posonlyargcount)
print(adder.__code__.co_stacksize)

unknown_bytes = adder.__code__.co_code
list_unknown_bytes = list(unknown_bytes)
code_len = len(list_unknown_bytes)

print(list_unknown_bytes)
# print(chr(124))
