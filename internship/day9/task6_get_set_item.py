class ShoppingCart:
    def __init__(self, items):
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value


cart = ShoppingCart(["Book", "Pen", "Notebook"])
print(cart[0])
cart[1] = "New Item"
print(cart[1])
