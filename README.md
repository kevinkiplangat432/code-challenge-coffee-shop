# Coffee Shop Domain Model

A Python domain model representing a Coffee Shop with Customers, Coffees, and Orders.
This project demonstrates object-oriented programming, relationships, aggregation, and class methods in Python.

### Overview

This project models a simple Coffee Shop domain using Python classes:

Customer – represents a customer of the coffee shop.

Coffee – represents a type of coffee available.

Order – represents a single order made by a customer for a coffee.

It captures real-world relationships:

A Customer can place multiple Orders.

A Coffee can have multiple Orders.

An Order belongs to one Customer and one Coffee.

The Order class acts as the single source of truth for all relationships.

### Features

1. Fully validated Customer and Coffee names.

2. Price validation for Orders.

3. Many-to-many relationships implemented through Order.

4. Aggregate methods:

5. Customer: list of coffees ordered

6. Coffee: total orders, average price

7. Class method most_aficionado(coffee) to identify the customer who spent the most on a given coffee.

8. Encapsulation and defensive copying for safe object state management.

Project Structure
coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
├── README.md
└── tests/

## Installation

##### Clone the repository:

**git clone https://github.com/kevinkiplangat432/code-challenge-coffee-shop.git**

cd coffee_shop


Set up a virtual environment with pipenv:

pipenv install
pipenv shell


Install pytest for testing:

pipenv install pytest


Create objects:

kevin = Customer("Kevin")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = kevin.create_order(latte, 5.0)
order2 = kevin.create_order(espresso, 4.5)

# Check customer's coffees
print(kevin.coffees())

# Coffee aggregate info
print(latte.num_orders())
print(latte.average_price())


Run all tests using pytest:

pytest tests/

License
MIT License
The license grants permission, free of charge, to any person obtaining a copy of the software and documentation files to deal in the Software without restriction, including the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies. All copies must include the copyright notice and license text. The software is provided "as is" without warranty, and the authors are not liable for claims, damages, or other liability. WVU Libraries libguides.wvu.edu/c.php?g=1260463&p=9239106 choosealicense.com 

Contributing

Contributions are welcome!

Fork the repository

## Author
Kevin kiplangat;