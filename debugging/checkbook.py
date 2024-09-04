class Checkbook:
    """
    A class representing a simple checkbook.

    Attributes:
    ----------
    balance : float
        The current balance in the checkbook.

    Methods:
    -------
    deposit(amount)
        Deposits the specified amount into the checkbook.
    withdraw(amount)
        Withdraws the specified amount from the checkbook if sufficient funds are available.
    get_balance()
        Prints the current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a new Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        ----------
        amount : float
            The amount to deposit.

        Example:
        -------
        >>> cb = Checkbook()
        >>> cb.deposit(100.0)
        Deposited $100.00
        Current Balance: $100.00
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds are available.

        Parameters:
        ----------
        amount : float
            The amount to withdraw.

        Example:
        -------
        >>> cb = Checkbook()
        >>> cb.deposit(100.0)
        Deposited $100.00
        Current Balance: $100.00
        >>> cb.withdraw(50.0)
        Withdrew $50.00
        Current Balance: $50.00
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Example:
        -------
        >>> cb = Checkbook()
        >>> cb.deposit(100.0)
        Deposited $100.00
        Current Balance: $100.00
        >>> cb.get_balance()
        Current Balance: $100.00
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    The main function that runs the checkbook program.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive number.")
                    else:
                        cb.deposit(amount)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive number.")
                    else:
                        cb.withdraw(amount)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()