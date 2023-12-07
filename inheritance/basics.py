# Inheritance:
##############
# 1. Inheritance means inheriting the properties and methods of a class into another class
# 2. Reusablity
# 3. REduce of code
# 4. Types of Inheritance
# 1. Single
# 2. multiple
# 3. multi-level
# 4. Hierarchical
# 5. Hybrid

# single Inheritance:
#######################
# 1. In single inheritance, we have only one base class and one derived class.
# 2. Derived or child class can inherit the properties and methods of the parent class
#
# class ParentClass:
#     def __init__(self, name, dept, age):
#         self.__name = name
#         self.__dept = dept
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_dept(self, dept):
#         self.__dept = dept
#
#     def get_dept(self):
#         return self.__dept
#
#     def get_details(self):
#         return f'User : {self.__name} and Branch : {self.__dept}'
#
#
# class ChildClass(ParentClass):
#     def __init__(self, name, dept, age):
#         super().__init__(name, dept, age)
#
#     def generate_username(self):
#         return super().get_name() + str(super().get_age())
#
#
# c1 = ChildClass("harish", 'CSE', 25)
# print(c1.get_name())
# print(c1.get_details())
# print(c1.generate_username())


# Multi-level inheritance
# 1. one parent, one child, one grandchild
#
# class University:
#     def __init__(self, name, no_of_colleges, total_academic_staff, total_adminstrative_staff):
#         self.__name = name
#         self.__no_of_colleges = no_of_colleges
#         self.__total_academic_staff = total_academic_staff
#         self.__total_adminstrative_staff = total_adminstrative_staff
#
#     def get_details(self):
#         return f'''
#             University Name : {self.__name}
#             No. of Colleges : {self.__no_of_colleges}
#             Total Academic staff : {self.__total_academic_staff}
#             Total Adminstrative staff : {self.__total_adminstrative_staff}
#         '''
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
#         return f'''
#             College Name : {self.__college_name}
#
#             College total Academic staff : {self.__college_total_academic_staff}
#             College total Adminstrative staff : {self.__college_total_adminstrative_staff}
#         '''
#
#
# c1 = College("SVU", 6, 1200, 1500, "SVU COllege of CM & CS", 24, 15)
#
# print(c1.get_details())
# # print(c1.get_university_details())
#
# # # MRO : Method resolution order
# print(College.__mro__)
#
#
# class Branch(College):
#     def __init__(self, name, no_of_colleges, total_academic_staff, total_adminstrative_staff, college_name,
#                  college_total_academic_staff, college_total_adminstrative_staff,
#                  branch_name, branch_code, no_of_students):
#         super().__init__(name, no_of_colleges, total_academic_staff, total_adminstrative_staff, college_name,
#                          college_total_academic_staff, college_total_adminstrative_staff)
#
#         self.__branch_name = branch_name
#         self.__branch_code = branch_code
#         self.__no_of_students = no_of_students
#
#     def get_details(self):
#         return f'''
#                 Branch Name: {self.__branch_name}
#                 Branch Code: {self.__branch_code}
#                 No. of students: {self.__no_of_students}
#             '''
#
#
# b1 = Branch("SVU", 6, 1200, 1500, "SVU COllege of CM & CS", 24, 15, "MCA", "SVUMCA0012", 118)
#
# print(b1.get_details())
#
# print(University.__mro__)
# print(College.__mro__)
# print(Branch.__mro__)


# multiple Inheritance
###########################
# two parents, one child

# class FruitShop:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#
#     def sell(self):
#         return f'''
#             From Fruit shop
#             {self.__name}, {self.__price}
#         '''
#
#
# class VegetableShop:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#
#     def sell(self):
#         return f'''
#             From Vegetable shop
#             {self.__name}, {self.__price}
#         '''
#
#
# class Store(FruitShop, VegetableShop):
#     def __init__(self, fruit_name, fruit_price, vegetable_name, vegetable_price):
#         FruitShop.__init__(self, fruit_name, fruit_price)
#         VegetableShop.__init__(self, vegetable_name, vegetable_price)
#
#     def sell(self):
#         fruits = FruitShop.sell(self)
#         vegetables = VegetableShop.sell(self)
#         return fruits, vegetables
#
#
# s1 = Store("Mango", 25, "Tomato", 15)
# print(s1.sell())


# Hierarchical Inheritance
##############################
# 1. one parent class, two or more child classes

# class A:
#     pass
#
# class B(A):
#     pass
#
# class c(A):
#     pass