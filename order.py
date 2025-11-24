from customer import Customer
from coffee import Coffee
class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer._add_order(self)
        coffee._add_order(self)

        # Append order to type class level list
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_object):
        if not isinstance(customer_object, Customer):
            raise TypeError("Order customer must be a Customer instance.")
        self._customer = customer_object

    @property
    def coffee(self):
        return self._coffee
    

    @coffee.setter
    def coffee(self, coffee_object):
        if not isinstance(coffee_object, Coffee):
            raise TypeError("Order coffee must be a Coffee instance.")
        self._coffee = coffee_object

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._price = float(price)
