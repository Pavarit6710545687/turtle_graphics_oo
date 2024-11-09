class Account:
    def __init__(self, num, account_type, name, init_balance):
        self.account_number = num
        self.account_type = account_type
        self.account_name = name
        self.balance = init_balance

    def deposit(self, amount):
        print(f"Depositing {amount} to {self.account_number}")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"Withdrawing {amount} from {self.account_number}")
            self.balance -= amount
        else:
            print(f"Withdrawal amount {amount} exceeds balance {self.balance} for {self.account_number}.")

    def show_details(self):
        print(f"Showing details for account {self.account_number}:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")


class AccountDatabase:
    def __init__(self):
        self.accounts = []

    def search_account(self, num):
        for index, account in enumerate(self.accounts):
            if account.account_number == num:
                return index
        return -1

    def create_account(self, num, account_type, name, init_balance):
        if self.search_account(num) == -1:
            account = Account(num, account_type, name, init_balance)
            self.accounts.append(account)
            print(f"Account {num} created.")
        else:
            print(f"Account {num} already exists.")

    def delete_account(self, num):
        index = self.search_account(num)
        if index != -1:
            print(f"Deleting account {self.accounts[index].account_number}.")
            del self.accounts[index]
        else:
            print(f"Account {num} does not exist; nothing to delete.")

    def show_account(self, num):
        index = self.search_account(num)
        if index != -1:
            self.accounts[index].show_details()
        else:
            print(f"Account {num} does not exist; nothing to show.")

    def deposit(self, num, amount):
        index = self.search_account(num)
        if index != -1:
            self.accounts[index].deposit(amount)
        else:
            print(f"Account {num} does not exist; no deposit action performed.")

    def withdraw(self, num, amount):
        index = self.search_account(num)
        if index != -1:
            self.accounts[index].withdraw(amount)
        else:
            print(f"Account {num} does not exist; no withdrawal action performed.")


# Example usage:
db = AccountDatabase()

# Creating accounts
db.create_account("0000", "saving", "David Patterson", 1000)
db.create_account("0001", "checking", "John Hennessy", 2000)
db.create_account("0003", "saving", "Mark Hill", 3000)
db.create_account("0004", "saving", "David Wood", 4000)

# Trying to create an already existing account
db.create_account("0004", "saving", "David Wood", 4000)

# Showing and modifying account details
db.show_account("0003")
db.deposit("0003", 50)
db.show_account("0003")
db.withdraw("0003", 25)
db.show_account("0003")
db.delete_account("0003")
db.show_account("0003")

# Trying operations on a deleted account
db.deposit("0003", 50)
db.withdraw("0001", 6000)
