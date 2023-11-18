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

lst = [2, 4, 5, 6]
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

# t = (x for x in range(5))
# print(t)








