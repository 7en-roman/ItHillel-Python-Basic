# ДЗ 12.2. Корзина для покупок

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.name}, Price = {self.price}'

class User:

    def __init__(self, name, surname, phonenumber):
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber

    def __str__(self):
        return f'{self.name} {self.surname}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        txt_ret = ''
        txt_ret += f'User: {self.user}\n'
        txt_ret += f'Items:\n'
        for product, amount in self.products.items():
            txt_ret += f'{product.name}: {amount} pcs.\n'
        return txt_ret

    def get_total(self):
        total_price = 0
        for product, amount in self.products.items():
            total_price += product.price * amount

        return total_price

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)

buyer = User("Roman", "Sushko", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)
"""
User: Roman Sushko
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)

print(cart)
"""
User: Roman Sushko
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
