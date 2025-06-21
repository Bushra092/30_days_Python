
#! dataclasses
#? It’s a decorator that automatically generates special methods for classes, such as:

from dataclasses import dataclass



@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0  # Default value

    def total(self):
        return 0
        return f'\n\nproduct name {self.name} \n\nProduct Price {self.price}\nproduct Quantity {self.quantity}\nTotal \t {self.price * self.quantity}'

item = Product(name="Pen", price=2.5)    #object Creation

# print(item)  #?Output: Product(name='Pen', price=2.5, quantity=0)

# Accessing fields
# print(item.name)      #? Pen
# print(item.quantity)  #? 0

# # Modifying values
# item.quantity = 25
# print(item)    #?  Product(name='Pen', price=2.5, quantity=25)

# print(item.total())

print('______________________________________________\nItem 2')
item2 = Product('Book', '7', '23')
print(item2)