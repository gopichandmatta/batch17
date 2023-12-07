# Polymorphism
###############
# The word polymorphism means having many forms.
# In programming, polymorphism means the same function name (but different signatures) being used for different types.
# The key difference is the data types and number of arguments used in function.
# 2 types:
# 1. static polymorphism: overloading
# 2. Dynamic polymorphism: Overriding

# Overloading:
###############
# 1. Operator loading:
######################
# + : Concatination
# * : Repitition

# print(3 + 5)
# print("harish" + "S")
#
# print(3 * 5)
# print("Harish" * 3)


# 2. Method overloading
########################
# 1. Same method name with different parameters
# 2. In python, method overloading is not possible
# 3. If you want to achieve there are 3 ways.
# 1. using variable-length arguments (*args)
# 2. using None value for variables
# 3. using @dispatch() method

# class Dummy:
#     def m1(self):
#         return "Hello"
#
#     def m1(self, name):
#         return f"Hello {name}"
#
#     def m1(self, name, greet):
#         return f"{greet} {name}"


# d = Dummy()
# d.m1()


# To handle method overloading using *args

# class Calculator:
#     def add(self, *args):
#         counter = 0
#         if len(args) == 0:
#             return counter
#         else:
#             for i in args:
#                 counter += i
#             return counter
#
#
# c1 = Calculator()
# print(c1.add(1, 2, 3))
# print(c1.add())
# print(c1.add(1,2,3,4,5,5,6))

# using none
# class Calculator:
#     def add(self, a=None, b=None, c=None, d=None):
#         if a is not None and b is not None and c is not None and d is not None:
#             return a + b + c + d
#         elif a is not None and b is not None and c is not None:
#             return a + b + c
#         elif a is not None and b is not None:
#             return a + b
#         elif a is not None:
#             return a
#         else:
#             return 0
#
#
# c1 = Calculator()
# print(c1.add(1,2,3,4))
# print(c1.add(1,3,4))
# print(c1.add(1,2))
# print(c1.add(1))
# print(c1.add())

# using dispatch
from multipledispatch import dispatch


# class Calculator:
#     @dispatch(int, int, int)
#     def add(self, a, b, c):
#         return a + b + c
#
#     @dispatch(int, int)
#     def add(self, a, b):
#         return a + b
#
#     @dispatch(int)
#     def add(self, a):
#         return a
#
#     @dispatch()
#     def add(self):
#         return 0


# c1 = Calculator()
# print(c1.add(1, 3, 4))
# print(c1.add(1, 2))
# print(c1.add(1))
# print(c1.add())

# Overriding:
#############
# 1. Overriding a method of parent class in a child class

# class University:
#     def __init__(self, name, no_of_colleges, total_academic_staff, total_adminstrative_staff):
#         self.__name = name
#         self.__no_of_colleges = no_of_colleges
#         self.__total_academic_staff = total_academic_staff
#         self.__total_adminstrative_staff = total_adminstrative_staff
#
#     def get_details(self):
#         return {
#             "University Name": self.__name,
#             "No. of Colleges": self.__no_of_colleges,
#             "Total Academic staff": self.__total_academic_staff,
#             "Total Adminstrative staff": self.__total_adminstrative_staff
#         }
#
#
# class College(University):
#     def __init__(self, name, no_of_colleges, total_academic_staff, total_adminstrative_staff, college_name,
#                  college_total_academic_staff, college_total_adminstrative_staff):
#         super().__init__(name, no_of_colleges, total_academic_staff, total_adminstrative_staff)
#         self.__college_name = college_name
#         self.__college_total_academic_staff = college_total_academic_staff
#         self.__college_total_adminstrative_staff = college_total_adminstrative_staff
#
#     def get_details(self):
#         # university_details = super().get_details()
#         college_details = {
#             "university_details": super().get_details(),
#             "College Name": self.__college_name,
#             "College total Academic staff": self.__college_total_academic_staff,
#             "College total Adminstrative staff": self.__college_total_adminstrative_staff
#         }
#         # details = {
#         #     "university_details": university_details,
#         #     "college_details": college_details
#         # }
#         return college_details
#
#
# c1 = College("SVU", 6, 1200, 1500, "SVU COllege of CM & CS", 24, 15)
# print(c1.get_details())
