import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product(
        name="Самсунг",
        description="серый цвет",
        price=180000.0,
        quantity=8,
    )


def test_product_init(product):
    assert product.name == "Самсунг"
    assert product.description == "серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 8


def test_quantity_is_integer():
    # Проверка, что quantity приводится к int (если передать float)
    product = Product("Мышь", "Беспроводная мышь", 2000, 10.9)
    assert isinstance(product.quantity, int)
    assert product.quantity == 10


def test_new_product_from_dict():
    data = {
        "name": "Клавиатура",
        "description": "Механическая клавиатура",
        "price": "5000",  # Передаем строкой, метод должен привести к float
        "quantity": "2",  # Передаем строкой, метод должен привести к int
    }
    product = Product.new_product(data)

    assert product.name == "Клавиатура"
    assert product.description == "Механическая клавиатура"
    assert product.price == 5000.0
    assert product.quantity == 2


def test_set_positive_price(product):
    product.price = 3500
    assert product.price == 3500


def test_set_zero_price_rejected(product, capsys):
    """Проверка, что при цене 0 выводится сообщение и цена не меняется"""
    original_price = product.price
    product.price = 0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price


def test_str_format_correct():
    product = Product("Кофемашина", "Автоматическая кофемашина", 45000.75, 3)
    result = str(product)
    expected = "Кофемашина, 45000.75 руб. Остаток: 3 шт."

    assert result == expected


def test_sum_product():
    """Проверка корректной работы метода add"""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    total1 = product1 + product2
    total2 = product1 + product3
    total3 = product2 + product3

    assert total1 == 2580000.0
    assert total2 == 1334000.0
    assert total3 == 2114000.0


def test_raises():
    with pytest.raises(ValueError):
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0
        )
