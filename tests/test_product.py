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
