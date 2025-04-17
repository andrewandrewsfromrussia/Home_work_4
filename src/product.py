class Product:
    """
    Описание класса.
    """

    # Атрибуты класса.
    # Свойства класса.
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        # Инициализация класса, передача значений атрибутов класса.
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
