# Abstraction:
###############
# 1.  Abstraction provides a programmer to hide all the irrelevant data/process of an
# application in order to reduce complexity and increase the efficiency of the program.
# 2. Achieved using abstract classes & abstract methods
# 3. Abstract classes: classes which contain abstract methods & static methods
# 4. Abstract methods: Methods which don't have any implementation.
from abc import ABC, abstractmethod


class Product(ABC):
    @staticmethod
    def purchase():
        return "Purchased"

    @abstractmethod
    def get_stock(self):
        pass

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Phone(Product):
    def __init__(self, name, price, discount, battery, storage, stock):
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__battery = battery
        self.__storage = storage
        self.__stock = stock

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_discount(self):
        return self.__discount

    def get_mobile_details(self):
        return f'''
            Mobile : {self.__name},
            Price : {self.__price},
            Discount: {self.__discount},
            Battery: {self.__battery},
            Storage : {self.__storage},
            Stock : {self.__stock}
        '''

realme = Phone("Realme", 13000, 8, 6000, "64gb", 100)
print(realme.get_stock())
print(realme.get_discount())
print(realme.get_price())
print(realme.get_mobile_details())
print(Phone.purchase())