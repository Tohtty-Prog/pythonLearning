class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
       if amount > 0:
           self.balance += amount
        
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance
    
        
def main():
    testAccount: BankAccount = BankAccount(1, 200)

    testAccount.deposit(100)
    print(testAccount.get_balance())
    testAccount.withdraw(350)
    print(testAccount.get_balance())
if __name__ == "__main__":
    main()