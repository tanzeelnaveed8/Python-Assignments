class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting the price...")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Test the class
p = Product(100)
print(p.price)       # Getting the price... ➜ 100

p.price = 150        # Setting the price...
print(p.price)       # Getting the price... ➜ 150

del p.price          # Deleting the price...


