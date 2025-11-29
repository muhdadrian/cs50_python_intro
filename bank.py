balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance # the solution to access to the global variable above
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()

"""
# using the word 'global' in front of balance inside both deposit and withdraw functions
to have access to the global variable of 'balance = 0' 
"""