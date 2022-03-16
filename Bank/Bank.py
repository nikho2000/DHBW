class Account:

    def __init__(self, username, password):
        self.balance = 0
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

    def whoami(self):
        print(
            "This is the account of: " + self.username + " with the password: " + self.password +
            " and a balance of: " + str(
                self.balance))


User = {}


def create_account(name, password):
    newaccount = Account(name, password)
    User[name] = newaccount
    return newaccount


def login(name, password):
    try:
        if password == User[name].get_pwd():
            return User[name]
    except KeyError:
        print("Wrong username or password!")
        return 0


def check_input(value):
    try:
        return float(value)
    except ValueError:
        print("Impossible transaction!")
        return 0.0


def safe_input(value):
    try:
        return input(value).split()
    except KeyboardInterrupt:
        exit()


def main():
    current_account = 0
    print("Welcome to your Favourite Bank. Type in What you want to do")

    while True:

        text = safe_input("Login -, Createaccount [Username] [Password] or Exit: ")

        if not len(text) == 3 and not text[0].lower() == "exit":
            print("Wrong command!")
            continue

        if text[0].lower() == "login":
            current_account = login(text[1], text[2])

        if text[0].lower() == "createaccount":
            if not text[1] in User:
                current_account = create_account(text[1], text[2])
                print("Your new account was created successfully.")
            else:
                print("Account already exists!")

        if text[0].lower() == "exit":
            exit()

        if current_account == 0:
            continue

        while True:
            eingabe = safe_input("Overview: Deposit [Amount], Withdraw [Amount], Balance, End: ")

            if len(eingabe) == 1:
                if eingabe[0].lower() == "balance":
                    current_account.current_balance()
                elif eingabe[0].lower() == "end":
                    current_account = 0
                    break

            elif len(eingabe) == 2:
                if eingabe[0].lower() == "deposit":
                    current_account.deposit(check_input(eingabe[1]))

                elif eingabe[0].lower() == "withdraw":
                    current_account.withdraw(check_input(eingabe[1]))
            else:
                print("Wrong input! try again or Exit with [Exit]")


main()
