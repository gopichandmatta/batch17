import sys

# age = 18
# name = "Harish"
# is_male = True
# com_dt = 3 + 4j
# price = 45.99
#
# print(type(age))
# print(isinstance(age,str))

# operators
# arithemetic operators: +, -, %, *, //,**,/
# num1 = -10
# num2 = 3
# print(num1/num2)
# print(num1//num2)
# relation or comparison operators
# ==, <=,>=, >,<<,!=
# logical
# and or not
# assignment operator
# =, +=, -=,/=,*=
# membership operator
# in , not in

# if 5 in (1,2,3,4):
#     print("present")
# else:
#     print("Not present")

# identity operator
# is , not is
# lst = [1,2,3]
# lst1=[1,2,3]
# print(id(lst))
# print(id(lst1))
# print(lst == lst1)
#
# print(lst is lst)

# data collections
# 1. list
# 2. tuple
# 3. dict
# 4. set
# 5. frozenset

# List:
# 1. collection of different data types
# 2. mutable
# 3. Indexing is possible
# 4. List is dynamic (size increases & decrease)
# 5. list is slower than tuple
# 6. List is less memory efficient than tuple
# 7. denoted by square braces
# 8. list compreshension is possible

# list creation
# lst = [1,3,"Harish",True]
# nested_list = [
#     [1,3],
#     [3,4]
# ]
#
# print(sys.getsizeof(lst))
#
# print(sys.getsizeof(4))

# lst = [2, 4, 5, 6]
# print(lst.append(7))
# # print(lst)
# print(lst.insert(2,"abc@gmail.com"))
# print(lst)
# print(lst.pop())
# print(lst.pop(3))

# lst.clear()
# print(lst)
# # print(lst.pop(2))
# lst.extend((1.2,3,4,5))
# print(lst)
# lst.append([1.2,3,4,5])
# print(lst)

# lst = [1, 2, 4, 5, 3, 5, 2]
# print(lst.sort(reverse=True))
# print(lst)

# sorted()
# 1. sorted() creates a new object
# 2. sorted() can be used with list, tup, dict (sequences)

# lst = [32, 22, 12, 44, 95, 111]
# print(sorted(lst, key=lambda x: str(x)[0]))

# lst = [1,2,0,4]
#
# lst1 = sorted(lst)
#
# lst.sort()
#
# print(id(lst))
# print(id(lst1))

# sort(), append(),extend(), insert(), pop(),index(), count()
#
# lst = [12,3,4,5]
# print(lst.index(4))
#
# print(lst.remove(4))

# list compreshension:

# lst = []
# for i in range(1,11):
#     lst.append(i)
#
# print(lst)
#
# lst = [i for i in range(1,11)]
# print(lst)

# list()
# lst = []
# lst = list({1,2,3,4})
# print(lst)

# aliasing vs cloning
# aliasing
# l = [1,2,3]
# l1 = l
# l[0]=100
# print(l1)

# cloning
# l = [1,2,3]
# l1 = l.copy()
# l[0]=100
# print(l1)

# shallow copy vs deep copy

# shallow copy
# l = [1,2,3,[3,4,5]]
# l1 = l.copy()
# l[3][1]=100
# print(l1)

# deep copy
# import copy
#
# l = [1,2,3,[3,4,5]]
# l1 = copy.deepcopy(l)
# l[3][1]=100
# print(l1)

# tuple
# 1. collection of different data types, similar to list
# 2. immutable
# 3. memory effficient than list
# 4. takes less memory than list
# 5. faster than list
# 6. tuple comprehesion is not possible, instead it returns a generator object.
# tuple()
# 7. denoted by parenthesis , ()

# lst = [1, 2, 3]
# tup = (1, 2,2, 3)
#
# print(len(tup))
# print(tup.count(2))
# print(sys.getsizeof(lst))
#
# print(sys.getsizeof(tup))

# tup1 = ("Harish", True, 23, 4.5)
# print(id(tup1))
# tup2 = ("Abc", False)
# tup1 += tup2
# print(id(tup1))
#
# t = (2,)
# print(type(t))
# print(t[0])
# t= (1,2,3)
# print(list(t))
# print(5 in t)
# t = (x for x in range(5))
# print(t)
# del t
#
# print(t)

# set
# 1. collection to store multiple objects of different datatypes
# 2. mutable
# 3. Unordered
# 4. contain unique elements
# 5. denoted by set() or {} ( should not be declared like s = {} )

# creating a set
# s = set()
# print(type(s))

# s = {1, 2, 3, 4, 3, 2, "abc"}

# print(int(False))

# print(s)
# accessing set value throws TypeError
# print(s[2])

# iterating over sets
# for i in s:
#     print(i)

# s = {1,2,3}
# s.add(4)
# print(s)
# s.update((5,6,4))
# print(s)
# print(s.pop())
# print(s.remove(4))
# print(s)
# print(s.discard(8))


# s1 = {1,2,3}
# s2 = {1,4,5,6}
#
# # union
# print(s1 | s2)
#
# # intersection
# print(s1 & s2)
#
# # difference
# print(s2 - s1)
#
# # symmetric diffeference
# print(s1.symmetric_difference(s2))

# s1 = {1,2,3,4,5}
# s2 = {2,3}
#
# print(s2.issubset(s1))
# print(s2.issuperset(s1))
#
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
#
# s = {1,'abc',4.5}
# print(len(s))

# Dictionaries:
# 1. Group of Key-value of pairs
# 2. Duplicate keys are not allowed but values can be duplicated
# 3. Any data type can be allowed as key & value
# 4. Dictionaries are ordered from python 3.7
# 5. Dictionaries are mutable so that we can add, delete, edit dictionaries
# 6. Dictionaries are dynamic
# 7. Keys should be immutable.

# user_info = {
#     "user_1234": {
#         "userid": "user_1234",
#         "username": "Harish@1234",
#         "name": "Harish",
#         "gender": "Male",
#         "age": 25
#     },
#     "user_3234": {
#         "userid": "user_3234",
#         "username": "Harish@1234",
#         "name": "Harish3",
#         "gender": "Male",
#         "age": 25
#     },
#     "user_1235": {
#         "userid": "user_1235",
#         "username": "Harish@2234",
#         "name": "Harish4",
#         "gender": "Male",
#         "age": 25
#     },
#     "user_1233": {
#         "userid": "user_1233",
#         "username": "Harish@1134",
#         "name": "Harish2",
#         "gender": "Male",
#         "age": 25
#     }
# }

# accessing values using keys
# print(user_info['user_1233'])
# print(user_info['user_1235'])

# dictionary methods
# update(), items(), values(), keys(), pop(),popitem(),get(),setdefault(), clear()

# creating empty dictionary
# 2ways
# d = {}
# d = dict()


# d = {
#     "name": "Harish",
# }
#
# additional_info = {"course": 'python',
#                     "webframework": "Django",
#                     "DB": ["POSTGRES", "MYSQL"]
#                    }
# d.update(additional_info)
# print(d)
#
# d = {
#     1: True,
#     2: False
# }
#
# d[1]="Hello"
#
# print(d)

# print(d[3]) #KeyError: 3
# val = d.get(1, "Key Not available")
# print(val)
# values = d.values()
# print(type(values))
# print(values)
#
# for value in values:
#     print(value)

# va = d.setdefault(2,"Harish")
# print(va)
# print(d)

# functions:
# Groups of statments
# Reusability
# types of functions
# 1. Built-in or pre-defined
# 2. user-defined

# creating a parameterless function
# def function_name():
#     print("Hi")
#     print("Good morning")
#     print("How r u")
#     print("Good Bye")
#
#
# # function calling
# function_name()
#
#
# # function with parameters
# def function_to_greet(name):
#     print(f"Hi {name}!")
#
#
# # arguments vs Parameters
# function_to_greet("Harish")
#
#
# def add(num1=1, num2=3):
#     print(num2 + num1)
#
#
# # positional argument
# add(3, 4)
#
# # default arguments
# add()
# add(1, 5)
#
# add(num2=10, num1=15)
#
#
# # variable-length & kwargs
#
# def display_sequence(*args):
#     print(args)
#     for i in args:
#         print(i)
#
#
# display_sequence(1, 2, 3, 0, 4, 89, 100)
#
#
# def display_keypairs(**args):
#     print(args)
#     for k, v in args.items():
#         print(k, v)
#
#
# display_keypairs(user="harish", userid=123)
# display_keypairs(user="harish1", userid=1234,gender="male")

# def generate_natural_nums(n):
#     lst = []
#     for i in range(n + 1):
#         lst.append(i)
#     return lst

# values = generate_natural_nums(10)
# print(values)

# a = 1,2,3,4
# print(a)
#
# def test():
#     return 1, 3, 5, 6
# print(test())

# Recursion:
# function calling itself is known as recursive function.
# this concept is called Recursion.

# adv:
# 1. clean code
# 2. reduce number of lines
# disadv:
# 1. not memory efficient
# 2. hard to debug

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))

# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(400))
# print(sys.getrecursionlimit())


# n = 10
#
#
# def test_func():
#     global n
#     n = 12
#     return n
#
#
# print(test_func())
# print(n)

# name = "harish"

# def test_func():
#     res = globals()
#     return res['name']
#
# print(test_func())

# namespace
# names of  identifiers
# LEGB

# Lambda Functions:
######################
# 1. Lambda functions are the ananonymous functions which do not have any name.
# 2. We can have any number of arguments and only one expression.
# 3. No return keyword
# 4. We can use lambda for short operations.
# 5. improves code readability and reduces the code.
# 6. mostly we use lambda functions with map, filter, reduce

# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# print(is_even_list[0]())
# for item in is_even_list:
# 	print(item)

# lam_fun = lambda x, y, z, k: (x * y * z) + k
#
# print(lam_fun(1, 2, 3, 4))

# ternary operator
# Trueresult if condition else falseresult
# Trueresult1 if condition else Trueresult2 if condition else FalseResult

# age = 2
# if age > 18:
#     print("eligible")
# else:
#     print("Not eligible")

# result = "Eligible" if age > 18 else "Not eligible"
# print(result)

# map(), filter(), reduct()
# 1. map()
###########
# syntax: map(func, seq)

# lst = [10, 20, 30, 40, 50]
# result = tuple(map(lambda x: x + 5, lst))
# print(result)

# names = ("harish", "dinesh", "naveen", "ratnam")
# emails = set(map(lambda name: name + "@ttt.com", names))
# print(emails)

# filter()
# syntax: filter(func, seq)
# import time

# number_list = [i for i in range(1, 10000000)]
# print(number_list)
#
# st = time.time()
# even_num_list = list(filter(lambda x: x % 2 == 0, number_list))
# odd_num_list = list(filter(lambda x: x % 2 != 0, number_list))
# et = time.time()
# print(et - st)
# print(even_num_list)
# print(odd_num_list)

# import time
# # #
# st = time.time()
# print(st)
# even_lst = []
# for i in number_list:
#     if i % 2 == 0:
#         even_lst.append(i)
# et = time.time()
# print(et)
# print(et - st)

# reduce
# syntax
# ===========
# from functools import reduce
# reduce(func, seq)

# from functools import reduce
#
# lst = [x for x in range(1, 11)]
# res = reduce(lambda a, b: a + b, lst, 5)
# print(res)
