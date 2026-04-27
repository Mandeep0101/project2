class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def show_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

# Main Program
atm = ATM(balance=1000)

print("Welcome to ATM")

if atm.check_pin():
    while True:
        atm.show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice! Try again.")
else:
    print("Incorrect PIN. Access Denied.")