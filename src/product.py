from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный класс
    """
    name: str
    description: str
    _price: float
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass


class MixinLog:
    """
    Класс миксин.
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        print(f"{repr(self)}")

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.name}, {self.description}, {self.price}, {self.quantity}"


class Product(MixinLog, BaseProduct):
    """
    Описание класса.
    """

    # Атрибуты класса.
    # Свойства класса.
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        # Инициализация класса, передача значений атрибутов класса.
        self.name = name
        self.description = description
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    # Магический метод str
    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    # Магический метод add
    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    # Метод создающий новый объект класса
    @classmethod
    def new_product(cls, product):
        return cls(**product)

    # Геттер для приватного аргумента цены
    @property
    def price(self):
        return self.__price

    # Сеттер для изменения цены
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        self.__price = new_price


class Smartphone(Product, MixinLog):
    """
    Описание класса.
    """

    # Свойства класса.
    efficiency: float
    model: str
    memory: int
    color: str

    # Переопределение метода инициализации с новыми атрибутами
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    # Переопределение метода класса
    def __add__(self, other):
        if type(other) is not Smartphone:
            raise TypeError

        return super().__add__(other)


class LawnGrass(Product, MixinLog):
    """
    Описание класса.
    """

    country: str
    germination_period: int
    color: str

    # Переопределение метода инициализации с новыми атрибутами
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # Переопределение метода класса
    def __add__(self, other):
        if type(other) is not LawnGrass:
            raise TypeError

        return super().__add__(other)
