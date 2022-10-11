# import os
# import numpy as np
# import pandas as pd
#
# import tempfile
#
# from rdkit import Chem
# from rdkit.Chem import AllChem
# import deepchem as dc
# import math
#
#
# #from deepchem.utils import download_url, load_from_disk
#
# def my_function(x = 3,y = 4):
#     z = math.sqrt(x**2+y**2)
#     return z
# print(my_function(7,10))
# from datetime import datetime
# start = datetime.now()
#
# def linear(a, b):
#     def result(x):              #在Python中，函数是可以嵌套定义的
#         return a * x + b
#     return result
# linear_01 = linear(2,3)
# print(linear_01(5))
# print(datetime.now()-start)
# from datetime import datetime
#
# time_start = datetime.now()
# def f2(n, i):
#     cache2 = dict()
#
#     def f(n, i):
#         if n == i or i == 0:
#             return 1
#         elif (n, i) not in cache2:
#             cache2[(n, i)] = f(n - 1, i) + f(n - 1, i - 1)
#         return cache2[(n, i)]
#
#     return f(n, i)
# outer_f = f2(100,10)
# print(outer_f)
# print(datetime.now() - time_start)

# from functools import lru_cache
# from datetime import datetime
#
# time_start = datetime.now()
# @lru_cache(maxsize=64)
# def cni(n, i):
#     if n==i or i==0:
#         return 1
#     return cni(n-1, i) + cni(n-1, i-1)
# print(cni(100,10))
# print(datetime.now() - time_start)

# decorate of python
# def print_func_name(func):
#     def warp():
#         print("Now use function '{}'".format(func.__name__))
#         func()
#     return warp
#
#
# @print_func_name
# def dog_bark():
#     print("Bark !!!")
#
#
# @print_func_name
# def cat_miaow():
#     print("Miaow ~~~")
#
#
# if __name__ == "__main__":
#     dog_bark()
#     # > Now use function 'dog_bark'
#     # > Bark !!!
#
#     cat_miaow()
#     # > Now use function 'cat_miaow'
#     # > Miaow ~~~

# # *args method
#
# # ex1: add numbers but can add two numbers
# def my_sum(a,b):
#     return a+b
# print(my_sum(2,3))
#
# # ex2 add more numbers
# def my_sum_more(my_integers):
#     result = 0
#     for x in my_integers:
#         result += x
#     return result
# list_of_integer = [1,2,3]
# print(my_sum_more(list_of_integer))
#
# # ex 3 use *args
# def my_sum_arg(*args): # The name of args is not important but the *
#     result = 0
#     # Iterating over the python args
#     for x in args: # unpacking operator (*), in tuple not list
#         result += x
#     return result
# print(my_sum_arg(2,3,4))

# **kwargs accept keyword arguments
# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values(): # Iterating over the keys of the Python kwargs dictionary
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
