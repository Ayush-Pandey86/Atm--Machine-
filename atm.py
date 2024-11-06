class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def inquire_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Balance inquiry")

    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrawn: ${amount}")

    def deposit_cash(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.transaction_history.append(f"Deposited: ${amount}")

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect old PIN.")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions to show.")
        else:
            print("Transaction history:")
            for transaction in self.transaction_history:
                print(transaction)


# Main program to interact with ATM functions
def atm_simulation():
    # Initialize account with default PIN '1234'
    account = BankAccount(pin='3395')
    
    print("Welcome to the ATM Machine!")
    entered_pin = input("Please enter your PIN: ")

    if not account.check_pin(entered_pin):
        print("Invalid PIN. Access Denied.")
        return

    while True:
        print("\nSelect an option:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account.inquire_balance()
        
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    account.withdraw_cash(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                else:
                    account.deposit_cash(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            old_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            account.change_pin(old_pin, new_pin)

        elif choice == '5':
            account.view_transaction_history()

        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the ATM simulation
atm_simulation()
