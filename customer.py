from coffee import Coffee
from customer import Customer

class Customer:
    all_customers = []
    def __init__(self, name):
        self.name =name  # for the setter methode
        self._orders = []  # to hold the orders of the customer
        Customer.all_customers.append(self)


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        #the validation takes two steps "string" of char "1 amd 15" i thought of combining thye cheker to a block but the user wont know what faile === no clarity hence the two validators.
        if not isinstance(name, str):

            raise ValueError("Customer name must be a string between 1 and 15 char.")

        if not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 char.")

        self._name = name


    
    #   - `orders()` method returns a list of all `Order` instances for that customer.
    #    - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

    def orders(self):
        # i returned a copy of the list so that the original is not touched.
        return list(self._orders)

    def coffees(self):
        #sets to clear out dups
        unique_list = {order.coffee for order in self._orders}
        return list(unique_list)
    