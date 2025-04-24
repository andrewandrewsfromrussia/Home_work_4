import pytest
from _pytest.capture import CaptureResult

from src.product import LawnGrass, Product, Smartphone


# Фикстура класса Product
@pytest.fixture
def product_one_init():
    return Product(
        "Xiaomi Redmi Note 11",
        "128GB, Pink Space",
        11000.0,
        14
    )


# Фикстура класса Product
@pytest.fixture
def product_two_init():
    return Product(
        "Xiaomi Redmi Note 12",
        "1024GB, Blue Sky",
        31000.0,
        8)


# Фикстура подкласса Smartphone
@pytest.fixture
def smartphone_one_init():
    return Smartphone(
        "Xiaomi 13 Pro",
        "Флагман с камерой Leica и мощным процессором Snapdragon 8 Gen 2",
        79990.0,
        8,
        91.2,
        "2210132G",
        256,
        "Ceramic White"
    )


# Фикстура подкласса Smartphone
@pytest.fixture
def smartphone_two_init():
    return Smartphone(
        "Sony Xperia 5 IV",
        "Компактный смартфон с OLED-дисплеем и улучшенной звуковой системой",
        74990.0,
        6,
        87.6,
        "XQ-CQ62",
        128,
        "Green"
    )


# Фикстура подкласса LawnGrass
@pytest.fixture
def lawngrass_one_init():
    return LawnGrass(
        "GreenLine Universal",
        "Газонная трава для универсального применения, устойчива к вытаптыванию",
        1290.0,
        10,
        "Германия",
        14,
        "Ярко-зелёный"
    )


# Фикстура подкласса LawnGrass
@pytest.fixture
def lawngrass_two_init():
    return LawnGrass(
        "AgroLux Shade",
        "Газон для затенённых участков, подходит для дачных участков и садов",
        990.0,
        5,
        "Россия",
        10,
        "Тёмно-зелёный"
    )


# Тест инициализации
def test_product_init(product_one_init) -> None:
    assert product_one_init.name == "Xiaomi Redmi Note 11"
    assert product_one_init.description == "128GB, Pink Space"
    assert product_one_init.price == 11000.0
    assert product_one_init.quantity == 14


# Тест добавления нового продукта из словаря
def test_new_product() -> None:
    product_test = {
        "name": "iPhone 14",
        "description": "Флагман от Apple с мощным процессором A15 Bionic",
        "price": 89990.0,
        "quantity": 10
    }

    product = Product.new_product(product_test)
    assert product.name == "iPhone 14"
    assert product.description == "Флагман от Apple с мощным процессором A15 Bionic"
    assert product.price == 89990.0
    assert product.quantity == 10


# Тест на обработку исключения ZeroDivisionError
def test_new_product_by_zero_quantity() -> None:
    product_test = {
        "name": "iPhone 14",
        "description": "Флагман от Apple с мощным процессором A15 Bionic",
        "price": 89990.0,
        "quantity": 0
    }
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product.new_product(product_test)


# Тест сеттера изменения цены с положительным значением
def test_positive_price_setter(product_one_init) -> None:
    product_one_init.price = 500
    assert product_one_init.price == 500.0


# Тест сеттера изменения цены с нулевым значением
def test_zero_price_setter(product_one_init) -> None:
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product_one_init.price = 0


# Тест сеттера изменения цены с отрицательным значением
def test_negative_price_setter(product_one_init) -> None:
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product_one_init.price = -1


# Тест метода str
def test_str_method(product_one_init) -> None:
    assert str(product_one_init) == "Xiaomi Redmi Note 11, 11000.0 руб. Остаток: 14 шт."


# Тест метода сложения класса Product
def test_add_method(product_one_init, product_two_init) -> None:
    assert product_one_init + product_two_init == 402000.0


# Тест метода сложения класса Smartphone и Smartphone
def test_add_smartphone_category(smartphone_one_init, smartphone_two_init) -> None:
    assert smartphone_one_init + smartphone_two_init == 1089860.0


# Тест метода сложения класса LawnGrass и LawnGrass
def test_add_lawngrass_category(lawngrass_one_init, lawngrass_two_init) -> None:
    assert lawngrass_one_init + lawngrass_two_init == 17850.0


# Тест метода сложения класса Smartphone и LawnGrass
def test_add_sp_to_lg_category(smartphone_one_init, lawngrass_one_init) -> None:
    with pytest.raises(TypeError):
        smartphone_one_init + lawngrass_one_init


def test_mixin(capsys, product_one_init):
    captured = capsys.readouterr()
    assert captured == CaptureResult(out='Product(Xiaomi Redmi Note 11, 128GB, Pink Space, 11000.0, 14\n', err='')
