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

# Most aficionado
print(Customer.most_aficionado(latte))

Class Descriptions
Customer

name – validated string (1–15 chars)

_orders – internal list of Order objects

Methods:

orders() – returns all orders for the customer

coffees() – returns unique list of Coffee instances

create_order(coffee, price) – creates a new order

most_aficionado(coffee) – class method identifying top spender for a coffee

Coffee

name – validated string (min 3 chars)

_orders – internal list of Order objects

Methods:

orders() – list of all orders for this coffee

customers() – unique list of customers who ordered

num_orders() – total orders

average_price() – average price of orders

Order

customer – Customer instance

coffee – Coffee instance

price – validated float (1.0–10.0)

Testing

Run all tests using pytest:

pytest tests/

License
MIT License
 – replace with your license.

Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Submit a pull request

Repository Link

Your Repository Here