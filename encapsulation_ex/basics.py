from logging.config import fileConfig

# Encapsulation:
####################

# 1. Wrapping of data and methods into one single unit called CLass.
# 2. We generaaly make variables or properties as private
# 3. And we can access those properties using methods.
# 4. use getter,setter methods to access and modify data.
# 5. provides security


# class BankAccount:
#     def __init__(self, account_no, account_holder_name, balance):
#         self.__account_no = account_no
#         self.__account_holder_name = account_holder_name
#         self.__balance = balance
#
#     def get_account_no(self):
#         return self.__account_no
#
#     def set_account_no(self, account_no):
#         self.__account_no = account_no
#
#     def __get_balance(self):
#         return self.__balance
#
#     def set_balance(self, balance):
#         self.__balance = balance
#
#     def set_account_holder_name(self, account_holder_name):
#         self.__account_holder_name = account_holder_name
#
#     def get_account_holder_name(self):
#         return self.__account_holder_name
#
#
# ac01 = BankAccount("111", "Harish", 1200)
# ac02 = BankAccount("112", "Harish2", 1200)
#
# print(ac01.get_account_holder_name())
# print(ac01.get_balance())
# print(ac01.get_account_no())
#
# ac01.set_account_holder_name("harish3")
# print(ac01.get_account_holder_name())