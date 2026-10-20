class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = int(quantity)

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        # Форматирование строки для одного товара
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def total_cost(self):
        """Возвращает общую стоимость этого товара на складе"""
        return self.price * self.quantity

    def __add__(self, other):
        """Вычисляет полную стоимость всех товаров на складе"""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары из разных классов")
        return self.total_cost() + other.total_cost()


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
