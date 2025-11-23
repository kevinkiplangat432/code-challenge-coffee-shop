class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_object):
        from customer import Customer
        if not isinstance(customer_object, Customer):
            raise TypeError("Order customer must be a Customer instance.")
        self._customer = customer_object

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_object):
        from coffee import Coffee
        if not isinstance(coffee_object, Coffee):
            raise TypeError("Order coffee must be a Coffee instance.")
        self._coffee = coffee_object

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_object):
        if not isinstance(price_object, (int, float)):
            raise TypeError("Price must be a number.")
        if not (1.0 <= float(price_object) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._price = float(price_object)
