import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def setup_method(self):
        Order.all = []
    
    def test_coffee_creation(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
    
    def test_short_name_fails(self):
        with pytest.raises(ValueError):
            Coffee("AB")
    
    def test_coffee_orders(self):
        customer = Customer("Emma")
        coffee = Coffee("Macchiato")
        Order(customer, coffee, 3.50)
        assert len(coffee.orders()) == 1
    
    def test_average_price(self):
        customer = Customer("Dan")
        coffee = Coffee("Americano")
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 5.0)
        assert coffee.average_price() == 4.0