from src.product import Product


class Category:
    """
    Описание класса.
    """

    # Атрибуты класса.
    category_count = 0
    product_count = 0

    # Свойства класса.
    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        # Инициализация класса, передача значений атрибутов класса.
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    # Магический метод
    def __str__(self):
        product_c = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {product_c} шт."

    # Геттер для приватного атрибута класса
    @property
    def products(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    # Метод для добавления продукта в атрибут products
    # update: добавлена проверка product на принадлежность к классу или подклассу
    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += product.quantity

    # Метод подсчета среднего ценника и обратки исключений
    def middle_price(self):
        try:
            result = sum(product.price for product in self.__products) / Category.product_count
        except ZeroDivisionError:
            return 0

        return round(result, 2)
