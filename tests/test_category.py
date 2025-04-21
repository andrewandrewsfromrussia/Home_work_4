import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_init():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product],
    )
    return category


def test_product_init(category_init) -> None:
    assert category_init.name == "Смартфоны"
    assert category_init.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_init.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert category_init.category_count == 1
    assert category_init.product_count == 8


def test_category_add_product(category_init) -> None:
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category_init.add_product(product)

    assert category_init.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category_init.product_count == 22


def test_str_method_total_quanity(category_init):
    assert str(category_init) == "Смартфоны, количество продуктов: 8 шт."


@pytest.fixture
def category_for_add_test():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Iphone 16", "512GB, Pink", 1210000.0, 3)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    return category


def test_add_method_products(category_for_add_test):
    assert category_for_add_test.products.product1 + category_for_add_test.products.product2 == 0
