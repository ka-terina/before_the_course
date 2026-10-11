import pytest

from src.category import Category


@pytest.fixture
def category():
    return Category(
        name="Смартфоны",
        description="Лучшее средство связи на расстоянии",
        products=[
            {
                "name": "Самсунг",
                "description": "серый цвет",
                "price": 180000.0,
                "quantity": 8,
            },
            {
                "name": "Айфон",
                "description": "черный цвет",
                "price": 200000.0,
                "quantity": 3,
            },
        ],
    )


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Лучшее средство связи на расстоянии"
    assert category.products == [
        {
            "name": "Самсунг",
            "description": "серый цвет",
            "price": 180000.0,
            "quantity": 8,
        },
        {
            "name": "Айфон",
            "description": "черный цвет",
            "price": 200000.0,
            "quantity": 3,
        },
    ]
    assert category.category_count == 1
    assert category.product_count == 2
