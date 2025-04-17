import pytest

from src.product import Product


@pytest.fixture
def product_init():
    return Product("Name", "Description", 100.0, 10)


def test_product_init(product_init) -> None:
    assert product_init.name == "Name"
    assert product_init.description == "Description"
    assert product_init.price == 100.0
    assert product_init.quantity == 10
