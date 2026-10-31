import pytest

from src.category import Category, Product


@pytest.fixture
def category():
    p1 = Product.new_product(
        {
            "name": "Самсунг",
            "description": "серый цвет",
            "price": 180000.0,
            "quantity": 8,
        }
    )
    p2 = Product.new_product(
        {
            "name": "Айфон",
            "description": "черный цвет",
            "price": 200000.0,
            "quantity": 3,
        }
    )
    return Category(
        name="Смартфоны",
        description="Лучшее средство связи на расстоянии",
        in_products=[p1, p2],
    )


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Лучшее средство связи на расстоянии"

    products_list = category.products

    expected_strings = [
        "Самсунг, 180000.0 руб. Остаток: 8 шт.",
        "Айфон, 200000.0 руб. Остаток: 3 шт.",
    ]

    assert products_list == expected_strings
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_middle_price(category):
    assert category.middle_price() == 34545.454545454544
