#1.
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful")
            print("Current Balance:", self.balance)
        else:
            print("Deposit amount must be greater than zero")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining Balance:", self.balance)
    def checkbalance(self):
        print("current balance=",self.balance)
account = BankAccount("admin", "1234", 1000)
attempts = 3
for i in range(attempts):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == account.username and password == account.password:
        print("Login Successful")
        account.checkbalance()
        while True:
            print("Menu")
            print("1.deposit")
            print("2.withdraw")
            print("3.checkbalance")
            print("4.exit")
            choice=int(input("enter a choice"))
            if choice==1:
                amount=int(input("enter the amount"))
                account.deposit(amount)
            elif choice==2:
                amount=int(input("enter the withdrawal amount"))
                account.withdraw(amount)
            elif choice==3:
                account.checkbalance()
            elif choice==4:
                print("thank you have a nice day")
                break
            else:
                print("invalid choice")
        break
    else:
        print("Invalid Username or Password")
        if i == attempts - 1:
            print("Account Blocked")
        else:
            print("Attempts Remaining:", attempts - i - 1)
  
