import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(scope="function")
def category():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "128GB, Pink Space", 11000.0, 14)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    return category


# Тест работоспособности функции
def test_product_init(category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 11000.0 руб. Остаток: 14 шт."
    )
    assert category.category_count == 1
    assert category.product_count == 22

    # Обнулил счетчик (происходит накопление).
    Category.product_count = 0


# Тест на добавление класса Product в список категорий и корректный подсчет продукта
def test_category_add_product(category) -> None:
    product = Product("Xiaomi Redmi Note 12", "1024GB, Blue Sky", 31000.0, 8)
    category.add_product(product)

    assert category.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 11000.0 руб. Остаток: 14 шт.\n"
        "Xiaomi Redmi Note 12, 31000.0 руб. Остаток: 8 шт."
    )
    assert category.product_count == 30


def test_category_add_non_product(category) -> None:
    product = {
        "name": "Кирпич печной",
        "description": "Прочный и жаростойкий строительный материал",
        "price": 22.0,
        "quantity": 5000
    }

    with pytest.raises(TypeError):
        category.add_product(product)


# Тест метода str
def test_category_str_product(category):
    assert str(category) == "Смартфоны, количество продуктов: 22 шт."
