import os
import json

from Python.Snackautomat.exceptions import OutOfStockError


class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def buy(self):
        if not self.amount == 0:
            self.amount -= 1
        else:
            raise OutOfStockError


class Snackautomat:

    def __init__(self):
        self.products = []
        self.fill_machine()

    def fill_machine(self):
        if not os.path.isfile("products.json"):
            with open("products.json", "x", encoding="utf-8") as file:
                product = [{"name": "Snickers", "price": 1.20, "amount": 10},
                           {"name": "Mars", "price": 1.20, "amount": 10},
                           {"name": "Gummibärchen", "price": 2.50, "amount": 10},
                           {"name": "Skittles", "price": 1.55, "amount": 10},
                           {"name": "Bifi", "price": 2.30, "amount": 10},
                           {"name": "Corny", "price": 2.20, "amount": 10},
                           {"name": "Bounty", "price": 1.40, "amount": 10},
                           {"name": "Knoppers", "price": 1.90, "amount": 10},
                           {"name": "Mentos", "price": 1.35, "amount": 10},
                           {"name": "Twix", "price": 1.20, "amount": 10}]
                json.dump(product, file)

        with open("products.json", "r", encoding="utf-8") as file:
            self.products = json.load(file)
        print(self.products)


    def run(self):
        pass


def safe_input(value):
    try:
        return input(value)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    snackautomat = Snackautomat()
    snackautomat.run()
