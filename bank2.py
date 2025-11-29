class Account:
    def __init__(self):
        self._balance = 0 # _ means private | instant variable

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account() # account object is calling the Account constructor
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()

"""
@ the instant variable of self._balance = 0 accessible by all the methods in the class by 
accessing it through the parameter of self.
"""
