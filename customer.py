
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

    def _add_order(self, order):
        self._orders.append(order)

    def orders(self):
        # i returned a copy of the list so that the original is not touched.
        return list(self._orders)

    def coffees(self):
        #sets to clear out dups
        unique_list = {order.coffee for order in self._orders}
        return list(unique_list)
    
    def create_order(self,coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        # validate it is a coffee instanxce
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Expected a Coffee instance.")
        
        # check if no orders
        if not coffee.orders():
            return None
        else:
            max_spent = 0
            top_customer = None
            for customer in cls.all_customers:
                spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
                if spent > max_spent:
                    max_spent = spent
                    top_customer = customer
        return top_customer



    