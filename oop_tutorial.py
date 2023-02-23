class Item():
    pay_rate = 0.8 # the pay rate after 20% discount

    # constructor
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f'price {price} is not greater than zero.'
        assert quantity >= 0, f'quantity {quantity} is not greater than zero.'

        # Assing to self object        
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * Item.pay_rate


# instantiating two objects
item1 = Item(name='Phone', price=100, quantity=2)
item2 = Item(name='Laptop', price=1000, quantity=3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(Item.__dict__) # all atributes for class level
print(item1.__dict__) # all atributes for instance level
print(item2.__dict__) # all atributes for instance level
item1.apply_discount()
print(item1.price)
