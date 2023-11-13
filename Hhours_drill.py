from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        
        self.balance = balance

    @abstractmethod
    def deposit(self,name, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal of ${:.2f} successful.".format(amount))
            else:
                print("Insufficient funds")
        else:
            print("Invalid amount for withdrawal")

class SavingsAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ${:.2f} successful.".format(amount))
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal of ${:.2f} successful.".format(amount))
            else:
                print("Insufficient funds")
        else:
            print("Invalid amount for withdrawal")

class BusinessAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ${:.2f} successful.".format(amount))
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal of ${:.2f} successful.".format(amount))
            else:
                print("Insufficient funds")
        else:
            print("Invalid amount for withdrawal")

def main():
    accounts = {}
    while True:
        ch = int(input('1: create account\n2: view account\n3: deposit\n4: withdraw\n5: delete account\n6: exit\n'))
        if ch == 1:
            accnum = input('Enter account number: ')
           
            account_type = input('Enter account type \n1:Checking \n2:Savings \n3:Business \n ')

            if account_type.lower() == '1':
                account = CheckingAccount(accnum)
            elif account_type.lower() == '2':
                account = SavingsAccount(accnum)
            elif account_type.lower() == '3':
                account = BusinessAccount(accnum)
            else:
                print("Invalid account type")
                continue

            accounts[accnum] = account
            print("Account created successfully!")

        elif ch == 2:
            accnum = input('Enter account number: ')
            account = accounts.get(accnum)
            if account:
                print(f"Account Number: {account.account_number}")
                print(f"Current Balance: ${account.get_balance()}")
            else:
                print("Account not found")

        elif ch == 3:
            accnum = input('Enter account number: ')
            account = accounts.get(accnum)
            if account:
                amount = float(input('Enter the deposit amount: $'))
                account.deposit(amount)
            else:
                print("Account not found")

        elif ch == 4:
            accnum = input('Enter account number: ')
            account = accounts.get(accnum)
            if account:
                amount = float(input('Enter the withdrawal amount: $'))
                account.withdraw(amount)
            else:
                print("Account not found")

        elif ch == 5:
            accnum = input('Enter account number: ')
            if accnum in accounts:
                del accounts[accnum]
                print(f"Account {accnum} deleted")
            else:
                print("Account not found")

        elif ch == 6:
            exit(0)

main()