class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:

    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        # Записываем или обновляем количество товара в корзине
        self.products[item] = cnt

    def get_total(self):
        # Пересчитываем общую стоимость: цена товара * количество
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        # Формируем список товаров с переходом на новую строку
        items_str = "\n".join(
            [f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()]
        )
        return f"User: {self.user}\nItems:\n{items_str}"


# Проверка работы классов и ассертов:

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Экземпляр класса User'
assert cart.get_total() == 60, "Всего 60"
assert cart.get_total() == 60, 'Должно оставаться 60!'

cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
print("\nВсе проверки успешно пройдены!")