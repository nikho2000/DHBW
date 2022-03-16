import os
import json


def safe_input(value):
    try:
        return input(value)
    except KeyboardInterrupt:
        exit()


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

    def __init__(self, name, balance):
        self.balance = balance
        self.username = name

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


class Snackautomat:

    def __init__(self):
        self.products = []
        self.users = []
        self.fill_machine()
        self.load_userdata()
        self.current_account = 0

    def fill_machine(self):
        if not os.path.isfile("products.json"):
            with open("products.json", "x", encoding="utf-8") as file:
                product = [{"name": "Snickers", "price": 1.2, "amount": 10, "id": 1},
                           {"name": "Mars", "price": 1.2, "amount": 10, "id": 2},
                           {"name": "Gummibärchen", "price": 2.5, "amount": 10, "id": 3},
                           {"name": "Skittles", "price": 1.55, "amount": 10, "id": 4},
                           {"name": "Bifi", "price": 2.3, "amount": 10, "id": 5},
                           {"name": "Corny", "price": 2.2, "amount": 10, "id": 6},
                           {"name": "Bounty", "price": 1.4, "amount": 10, "id": 7},
                           {"name": "Knoppers", "price": 1.9, "amount": 10, "id": 8},
                           {"name": "Mentos", "price": 1.35, "amount": 10, "id": 9},
                           {"name": "Twix", "price": 1.2, "amount": 10, "id": 10}]
                json.dump(product, file)

        with open("products.json", "r", encoding="utf-8") as file:
            self.products = json.load(file)

    def load_userdata(self):
        if not os.path.isfile("userdata.json"):
            with open("userdata.json", "x", encoding="utf-8") as userdata:
                user = [{"name": "admin", "password": "admin", "balance": 10000000}]
                json.dump(user, userdata, indent=4)

        with open("userdata.json", "r", encoding="utf-8") as userdata:
            self.users = json.load(userdata)

    def create_account(self, name, password):
        if not os.path.isfile("userdata.json"):
            self.load_userdata()
            return False
        self.users.append({"name": name, "password": password, "balance": 0})
        with open("userdata.json", "w", encoding="utf-8") as userdata:
            json.dump(self.users, userdata, indent=4)
        card = Keycard(name, 0)
        return card

    def check_account(self, name):
        if not os.path.isfile("userdata.json"):
            self.load_userdata()
        for user in self.users:
            if name == user["name"]:
                return True
        return False

    def check_password(self, name, password):
        if not os.path.isfile("userdata.json"):
            self.load_userdata()
        for user in self.users:
            if password == user["password"] and name == user["name"]:
                return True
        return False

    def print_users(self):
        for user in self.users:
            print(user)

    def login_account(self, name, password):
        if not os.path.isfile("userdata.json"):
            self.load_userdata()
        for user in self.users:
            if name == user["name"] and password == user["password"]:
                card = Keycard(name, user["balance"])
                return card

    def list_products(self):
        for product in self.products:
            if product["amount"] == 0:
                print("ID | " + str(product["id"]) + " | " + str(product["name"]) +
                      " | Price: " + str(product["price"]) + " | Out of Stock")
            else:
                print("ID | " + str(product["id"]) + " | " + str(product["name"]) +
                      " | Price: " + str(product["price"]) + " | Amount: " +
                      str(product["amount"]))

    def run(self):
        while True:
            print("============================================================")
            print("| Put in your Keycard and choose on of the following options")
            print("| Type in: [1] | login")
            print("|          [2] | create a new User")
            print("|          [3] | list products")
            print("============================================================")
            data = safe_input("Choose between the given options: ").split()

            if not len(data) == 1:
                print("Invalid! Please choose between the given Options 1-3")
                continue

            if len(data) == 1:
                if not (data[0] == "1" or data[0] == "2" or data[0] == "3"):
                    print("Please choose a number between 1 and 3")
                    continue

                if data[0] == "1":
                    data = safe_input("Put in your data [username] [password]: ").lower().split()
                    if not len(data) == 2:
                        continue
                    if not self.check_password(data[0], data[1]):
                        print("Your username or password are incorrect!")
                        continue
                    self.current_account = self.login_account(data[0], data[1])
                    print("Account successfully logged in")

                if data[0] == "2":
                    data = safe_input("Put in your wished data [username] [password]: ").lower().split()
                    if not len(data) == 2:
                        continue
                    if self.check_account(data[0]):
                        print("Account already exists! ")
                        continue
                    self.current_account = self.create_account(data[0], data[1])
                    print("Account successfully created")
                if data[0] == "3":
                    print("============================================================")
                    self.list_products()
                    continue

                while True:
                    print("============================================================")
                    print("| Welcome: " + str(self.current_account.username))
                    print("| Type in: [1] | Deposit balance")
                    print("|          [2] | Show current balance")
                    print("|          [3] | List products")
                    print("|          [4] | Buy products by ID")
                    print("|          [5] | Logout")
                    print("============================================================")
                    data = safe_input("Input: ").lower().split()
                    if not len(data) == 1:
                        if not (data[0] == "1" or data[0] == "2" or data[0] == "3"):
                            print("Please choose a number between 1 and 3")
                            continue


if __name__ == "__main__":
    snackautomat = Snackautomat()
    snackautomat.run()
