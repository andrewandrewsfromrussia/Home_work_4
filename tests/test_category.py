import pytest

from src.category import Category


@pytest.fixture
def category_init():
    return Category("Name", "Description", ["One", "Two"])


def test_product_init(category_init) -> None:
    assert category_init.name == "Name"
    assert category_init.description == "Description"
    assert category_init.products == ["One", "Two"]
    assert category_init.category_count == 1
    assert category_init.product_count == 2
