"""
Snackautomat
"""

import os
import json
import sys


def safe_input(value):
    """
    Überprüft ob der Input abgebrochen wird, und beendet das Programm wenn dies geschieht
    :param value:
    :return:
    """

    try:
        return input(value)
    except KeyboardInterrupt:
        sys.exit()


def check_input(value):
    """
    Wandelt die Übergebene Variable wenn möglich in einen Float ansonsten wird 0 ausgegeben
    :param value:
    :return:
    """

    try:
        return float(value)
    except ValueError:
        return 0.0


class Snackautomat:
    """
    Klasse Snackautmat
    """
    def __init__(self):
        """
        Konstruktor des Snackautomaten, deklariert alle benötigten variablen
        """

        self.products = []
        self.users = []
        self.check_products()
        self.load_products()
        self.check_userdata()
        self.load_userdata()
        self.current_account = 0

    def check_products(self):
        """
        Überprüft ob eine products.json datei vorhanden ist
        :return:
        """

        if not os.path.isfile("products.json"):
            self.create_products()

    def create_products(self):
        """
        erstellt eine vorgefertigte products.json datei, und ließt den Wert in die products variable
        :return:
        """

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

    def load_products(self):
        """
        ließt den aktuellen stand der products.json Datei in die products variable ein
        :return:
        """

        with open("products.json", "r", encoding="utf-8") as products:
            self.products = json.load(products)

    def update_products(self):
        """
        Schreibt den aktuellsten Stand der products variable in die products.json
        :return:
        """

        self.check_products()
        with open("products.json", "w", encoding="utf-8") as products:
            json.dump(self.products, products)

    def check_userdata(self):
        """
        Überprüft ob die userdata.json Datei vorhanden ist
        :return:
        """

        if not os.path.isfile("userdata.json"):
            self.create_userdata()

    def create_userdata(self):
        """
        Erstellt eine userdata.json mit bsp. Benutzer und liest diese in die users variable ein
        :return:
        """

        with open("userdata.json", "x", encoding="utf-8") as userdata:
            user = [{"name": "admin", "password": "admin", "balance": 10000000}]
            json.dump(user, userdata, indent=4)

        with open("userdata.json", "r", encoding="utf-8") as userdata:
            self.users = json.load(userdata)

    def load_userdata(self):
        """
        Ließt den aktuellsten Stand der userdata.json in die users variable ein
        :return:
        """

        with open("userdata.json", "r", encoding="utf-8") as userdata:
            self.users = json.load(userdata)

    def update_user(self):
        """
        Schreibt den aktuellsten Stand der users Variable in die userdata.json
        :return:
        """

        self.check_userdata()
        with open("userdata.json", "w", encoding="utf-8") as userdata:
            json.dump(self.users, userdata, indent=4)

    def create_account(self, name, password):
        """
        Erstellt einen Benutzer und speichert ihn in die userdata.json
        :param name:
        :param password:
        :return:
        """

        self.check_userdata()
        self.users.append({"name": name, "password": password, "balance": 0})
        self.update_user()
        return name

    def check_account(self, name):
        """
        Überprüft ob ein Benutzer in der userdata.json vorhanden ist
        :param name:
        :return:
        """

        self.check_userdata()
        for user in self.users:
            if name == user["name"]:
                return True
        return False

    def check_password(self, name, password):
        """
        Überprüft ob das Zugehörige Passwort zu einem Benutzer korrekt ist
        :param name:
        :param password:
        :return:
        """

        self.check_userdata()
        for user in self.users:
            if password == user["password"] and name == user["name"]:
                return True
        return False

    def login_account(self, name, password):
        """
        Wenn die Eingegeben Benutzerdaten korrekt sind, wird der Name des Benutzers returnt
        :param name:
        :param password:
        :return:
        """

        self.check_userdata()
        for user in self.users:
            if name == user["name"] and password == user["password"]:
                return name

    def list_products(self):
        """
        Gibt jedes Produkt aus der products Variable aus
        :return:
        """

        for product in self.products:
            if product["amount"] == 0:
                print("| ID | " + str(product["id"]) + " | " + str(product["name"]) +
                      " | Price: " + str(product["price"]) + " | Out of Stock")

            else:
                print("| ID | " + str(product["id"]) + " | " + str(product["name"]) +
                      " | Price: " + str(product["price"]) + " | Amount: " +
                      str(product["amount"]))

    def outsourced_for_pylint(self, product):
        """
        Outsourced Function damit pylint nicht rumheult
        :param product:
        :return:
        """

        for user in self.users:
            if not user["name"] == self.current_account:
                continue
            user["balance"] = user["balance"] - product["price"]
            print("| Your new balance: " + str(user["balance"]))
            self.update_user()
            self.update_products()
            break

    def run(self):
        """
        Programmablauf des Snackautomaten
        :return:
        """

        while True:
            print("============================================================")
            print("| Put in your Keycard and choose on of the following options")
            print("| Type in: [1] | login")
            print("|          [2] | create a new User")
            print("|          [3] | list products")
            print("|          [4] | Exit")
            print("============================================================")

            data = safe_input("| Choose between the given options: ").split()

            if not len(data) == 1:
                print("Invalid! Please choose between the given Options 1-3")
                continue

            if not (data[0] == "1" or data[0] == "2" or data[0] == "3" or
                    data[0] == "4"):
                print("Please choose a number between 1 and 4")
                continue

            if data[0] == "1":
                data = safe_input("Put in your data [username] " +
                                  " [password]: ").lower().split()
                if not len(data) == 2:
                    continue
                if not self.check_password(data[0], data[1]):
                    print("Your username or password are incorrect!")
                    continue
                self.current_account = self.login_account(data[0], data[1])
                print("Account successfully logged in")

            if data[0] == "2":
                data = safe_input("Put in your wished data [username] " +
                                  " [password]: ").lower().split()
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

            if data[0] == "4":
                sys.exit()

            while True:
                print("============================================================")
                print("| Welcome: " + self.current_account)
                print("| Type in: [1] | Deposit balance")
                print("|          [2] | Show current balance")
                print("|          [3] | List products")
                print("|          [4] | Buy products by ID")
                print("|          [5] | Logout")
                print("============================================================")

                data = safe_input("| Choose between the given options: ").split()

                if not len(data) == 1:
                    print("Invalid! Please choose between the given Options 1-3")
                    continue

                if not (data[0] == "1" or data[0] == "2" or data[0] == "3" or
                        data[0] == "4" or data[0] == "5"):
                    continue

                if data[0] == "1":
                    data = safe_input("| Type in the amount you wish to deposit: ").split()
                    if not len(data) == 1:
                        continue
                    self.check_userdata()
                    for user in self.users:
                        if not user["name"] == self.current_account:
                            continue
                        user["balance"] = user["balance"] + check_input(data[0])
                        print("| Your new balance: " + str(user["balance"]))
                        self.update_user()
                        break

                if data[0] == "2":
                    if not len(data) == 1:
                        continue
                    self.check_userdata()
                    for user in self.users:
                        if user["name"] == self.current_account:
                            print("| Your current balance: " + str(user["balance"]))

                if data[0] == "3":
                    if not len(data) == 1:
                        continue
                    self.list_products()

                if data[0] == "4":
                    data = safe_input("| Type in the product ID: ").split()
                    if not len(data) == 1:
                        continue
                    _id = check_input(data[0])
                    for product in self.products:

                        if not check_input(product["id"]) == _id:
                            continue
                        if not product["amount"] > 0:
                            break
                        product["amount"] = product["amount"] - 1
                        self.outsourced_for_pylint(product)
                        break

                if data[0] == "5":
                    self.current_account = 0
                    break


if __name__ == "__main__":
    snackautomat = Snackautomat()
    snackautomat.run()
