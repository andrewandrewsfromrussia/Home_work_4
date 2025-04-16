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
    products: list

    def __init__(self, name, description, products):
        # Инициализация класса, передача значений атрибутов класса.
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
