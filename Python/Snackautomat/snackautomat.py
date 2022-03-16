import os
import json


class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def buy(self):
        if not self.amount == 0:
            self.amount -= 1
        else:
            print("There ist no item left to buy!")


class Keycard:

    def __init__(self, username, password, balance):
        self.balance = balance
        self.username = username
        self.password = password

    def get_pwd(self):
        return self.password

    def set_pwd(self, password):
        self.password = password

    def deposit(self, amount):
        if not amount == 0.0:
            self.balance += amount
            print("Your new balance: " + str(self.balance) + "$")

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Not enough balance!")
        else:
            self.balance -= amount
            print("Your new balance: " + str(self.balance) + "$")

    def current_balance(self):
        print("Current balance of your account:  " + str(self.balance) + "$")


User = {}


def login(name, password):
    try:
        if password == User[name].get_pwd():
            return User[name]
    except KeyError:
        print("Wrong username or password!")
        return 0


def safe_input(value):
    try:
        return input(value)
    except KeyboardInterrupt:
        exit()


class Snackautomat:

    def __init__(self):
        self.products = []
        self.users = []
        self.fill_machine()
        self.load_userdata()

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

    def load_userdata(self):
        if not os.path.isfile("userdata.json"):
            with open("userdata.json", "x", encoding="utf-8") as file:
                user = {"name": "admin", "password": "admin", "balance" : 10000000}
                json.dump(user, file)

            with open("userdata.json", "r", encoding="utf-8") as file:
                self.users = json.load(file)

    def create_account(self, name, password):
        try:
            with open("userdata.json", "x", encoding="utf-8") as file:
                user = {"name": name, "password": password, "balance": 0}
                json.dump(user, file)
        except FileNotFoundError:
            self.load_userdata()

    def check_account(self, name):
        try:
            with open("userdata.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                if 'name' in users == name:
                    return True
        except FileNotFoundError:
            self.load_userdata()

    def check_password(self, password):
        try:
            with open("userdata.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                if 'password' in users == password:
                    return True
        except FileNotFoundError:
            self.load_userdata()

    def login_account(self, name, password):
        pass

    def run(self):
        print("=================================")
        print("|            Welcome            |")
        print("| Type in: 1 | login keycard    |")
        print("|          2 | create a keycard |")
        print("|          3 | list products    |")
        print("=================================")
        while True:
            current_account = 0
            eingabe = safe_input("Input: ").split()

            if not len(eingabe) == 1:
                print("Invalid! Please choose between the given Options 1-3")
                continue

            if len(eingabe) == 1:
                if not (eingabe[0] == "1" or eingabe[0] == "2" or eingabe[0] == "3"):
                    print("dumb")
                    continue

                if eingabe[0] == "1":
                    data = safe_input("Put in your data [username] [password]: ").split()

                if eingabe[0] == "2":
                    data = safe_input("Put in your wished data [username] [password]: ").split()
                    self.create_account(data[0], data[1])


if __name__ == "__main__":
    snackautomat = Snackautomat()
    snackautomat.run()
