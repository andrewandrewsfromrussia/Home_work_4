import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.product_count = 0
    Category.category_count = 0


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


@pytest.fixture(scope="function")
def empty_category():
    category = Category(
        "Ничего",
        "Здесь абсолютно ничего нет",
        []
    )

    return category


# Тест инициализации функции
def test_product_init_name(category) -> None:
    assert category.name == "Смартфоны"


# Тест инициализации функции
def test_product_init_description(category) -> None:
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )


# Тест инициализации функции
def test_product_init_products(category) -> None:
    assert category.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 11000.0 руб. Остаток: 14 шт."
    )


# Тест инициализации функции
def test_product_init_category_count(category) -> None:
    Category.category_count = 1
    assert category.category_count == 1


# Тест инициализации функции
def test_product_init_product_count(category) -> None:
    assert category.product_count == 22


def test_product_init_product_count_zero(category) -> None:
    # Обнулил счетчик (происходит накопление).
    Category.product_count = 0
    assert Category.product_count == 0


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


# Тест на добавление неверного класса
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


# Test average_price method
def test_average_price_sum(category):
    assert category.middle_price() == 83363.64


# Test ZeroDivisionError
def test_average_price_empty_list(empty_category):
    assert empty_category.middle_price() == 0
