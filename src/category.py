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
        Category.product_count += len(products)

    # Геттер для приватного атрибута класса
    @property
    def products(self):
        return "\n".join(
            f"{product.name}, " f"{product.price} руб. Остаток: " f"{product.quantity} шт."
            for product in self.__products
        )

    # Метод для добавления продукта в атрибут products
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
