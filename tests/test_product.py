import pytest

from src.product import Product


@pytest.fixture
def product_init():
    return Product("Name", "Description", 100.0, 10)


@pytest.fixture
def product_add_fixture():
    return Product("Name2", "Description2", 80.0, 4)


def test_product_init(product_init) -> None:
    assert product_init.name == "Name"
    assert product_init.description == "Description"
    assert product_init.price == 100.0
    assert product_init.quantity == 10


def test_new_product() -> None:
    product_test = {"name": "iPhone 15", "description": "128GB, Черный", "price": 210000.0, "quantity": 8}

    product = Product.new_product(product_test)
    assert product.name == "iPhone 15"
    assert product.description == "128GB, Черный"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter(product_init):

    product_init.price = 500
    assert product_init.price == 500.0

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product_init.price = 0

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product_init.price = -1


def test_str_method(product_init) -> None:
    assert str(product_init) == "Name, 100.0 руб. Остаток: 10 шт."


def test_add_method(product_init, product_add_fixture) -> None:
    assert product_init + product_add_fixture == 1320.0