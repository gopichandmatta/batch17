# Different programming paradigms:
# 1. procedural-oriented programming
# 2. Functional programming
# 3. Object-oriented programming


# OOPs : Object oriented Programming
# OOPS is a paradigm or process to solve real world problems.
# OOPS provides code maintainance, Security, modularity, efficiency.
# Partially OOP

# Principles of OOPS
####################
# 1. Encapsulation
# 2. Polymorphism
# 3. Inheritance
# 4. Abstraction

# Classes & objects:
######################
# Class:
# 1. class is collection of properties(variables) and behavior (methods)
# 2. Using classes we create instances or objects


# class Car:
#     def __init__(self, color, price, engine, name, brand):
#         # instance variables
#         self.color = color
#         self.price = price
#         self.engine = engine
#         self.name = name
#         self.brand = brand
#
#     def start(self):
#         pass
#
#     def stop(self):
#         pass
#
#
# innova = Car("white", "1500000", "3500HP", "Innova", "TOYOTA")
# kia = Car("black", "1000000", "3500HP", "Kia", "Kia")
#
# print("Innova information")
# print(f"""
#     Name : {innova.name}
#     Brand : {innova.brand}
#     Price : {innova.price}
#     engine : {innova.engine}
# """)
#
# print(id(innova))
# print(id(kia))
# kia.name = "Suzuki"
#
# print("Kia information")
# print(f"""
#     Name : {kia.name}
#     Brand : {kia.brand}
#     Price : {kia.price}
#     engine : {kia.engine}
# """)
# print(innova.name)
#
# print(isinstance(kia, Car))


# constructors
##################
# def __init__(self):
# constructors are the special methods which can be called whenever the object is created.
# two types of constructors:
# 1.default constructor or parameterless constructor
# 2. Parameterized constructor

# class Car:
#     def start(self):
#         pass
#
#     def stop(self):
#         pass
#
#
# obj = Car()
# print(obj)

# class Student:
#     def __init__(self):
#         pass

# types of variables in OOPS:
###############################
# 1. instance variables
# 2. static variables or class varibles: Memory efficiency

# class College:
#     # static or class variable
#     principal = "John"
#
#     def __init__(self, dept, adminstrative_staff, academic_staff):
#         # instance variables
#         self.dept = dept
#         self.adminstrative_staff = adminstrative_staff
#         self.academic_staff = academic_staff
#
#
# ece = College("ECE", 30, 10)
# cec = College("CEC", 20, 8)
#
# print(College.principal)
# print(ece.principal)
# print(cec.principal)
#
# College.principal = "Murthy"
# print(College.principal)
# print(ece.principal)
# print(cec.principal)


# types of methods
####################

# 1. instance methods
# Instance method contains self as a first argument
# It is used to perform any action on objects of the class.

# 2. static methods
# A static method does not receive an implicit first argument.
# A static method is also a method that is bound to the class and not the object of the class.
# This method can’t access or modify the class state.
# It is present in a class because it makes sense for the method to be present in class.

# 3. class methods
# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.

# class Bank:
#     country = "India"
#
#     def __init__(self):
#         pass
#
#     def withdraw(self):
#         pass
#
#     def deposit(self):
#         pass
#
#     def check_balance(self):
#         pass
#
#     @staticmethod
#     def static_method_ex():
#         pass
#
#     @classmethod
#     def class_method_ex(cls):
#         pass
