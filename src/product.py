class Product:
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
        self.__price = price
        self.quantity = quantity

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
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
