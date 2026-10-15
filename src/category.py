from src.product import Product


class Category(Product):
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name, description, in_products=None):
        self.name = name
        self.description = description

        if in_products is None:
            self.__products = []
        else:
            self.__products = list(in_products)

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def set_products(self, products):
        self.__products = products

    def add_product(self, product_obj):
        """Метод для добавления товара в категорию"""
        if isinstance(product_obj, Product):
            self.__products.append(product_obj)
            Category.category_count += 1
        else:
            raise TypeError("В категорию можно добавить только объект класса Product")

    @property
    def products(self):
        """Геттер, возвращающий список товаров в виде строк."""
        return [str(product) for product in self.__products]
