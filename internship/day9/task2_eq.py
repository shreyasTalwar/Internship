class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Mobile):
            return NotImplemented
        return (self.brand, self.model) == (other.brand, other.model)


m1 = Mobile("Apple", "iPhone 15", 90000)
m2 = Mobile("Apple", "iPhone 15", 85000)
m3 = Mobile("Samsung", "S24", 80000)

print(m1 == m2)
print(m1 == m3)
print(m2 == m3)
