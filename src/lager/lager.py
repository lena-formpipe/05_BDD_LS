# kod för lagerhållning


class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Stock:
    def __init__(self):
        self.items = []


    def add_product(self, product):
        self.items.append(product)


    def increase_quantity(self, name, amount):
        # ökar antal om varan finns, annars skapa varan
        product = self.get_product(name)
        if product is not None:
            product.amount += amount
        else:
            self.add_product(StockItem(name, amount))


    def get_product(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def decrease_quantity(self, name, amount):
        # minskar antal om varan finns
        product = self.get_product(name)
        if product is not None:
            product.amount -= amount
        return None