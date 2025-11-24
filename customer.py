from coffee import Coffee
from customer import Customer

class Customer:
    all_customers = []
    def __init__(self, name):
        self.name =name  # for the setter methode
        self._oders = []  # to hold the orders of the customer
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


    


    