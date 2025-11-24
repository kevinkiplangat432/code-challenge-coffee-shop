from order import Order
from customer import Customer

class Coffee:
    def __init__(self, coffee_name ):
        self.coffee_name = coffee_name # for the setter:

    @property
    def coffee_name(self):
        return self._coffee_name
    

    @coffee_name.setter
    def coffee_name(self, coffee_name):
        # again same brains ...validation be clear ..whats failing stirng or char
        if not isinstance(coffee_name, str):

            raise ValueError(f"The name: {coffee_name} must be a string")
        
        if not len(coffee_name) >3:
            raise ValueError(f"the name: {coffee_name} must be of more than 3 char")
        
        self._coffee_name = coffee_name
    

    def _add_order(self, order):
        pass
