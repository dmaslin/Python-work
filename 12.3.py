class Bank:
    def __init__(self, accounts):
        self.__accounts = accounts
    def menu(self):
        while True:
            print("")
            print("Main Menu \n1: check balance \n2: withdrawl \n3: deposit \n4: exit")
            x = eval(input("Enter a choice: "))
            if x == 1:
                self.balance()
            elif x == 2:
                self.withdrawl()
            elif x == 3:
                self.deposit()
            elif x == 4:
                return True
            else:
                print("Sorry that isn't a valid input please try again")
    def user(self):
        while True:
            self.user = eval(input("Enter an account id: "))
            if self.user > 9:
                print("Sorry that is an invalid account id. Please try again")
            else:
                self.menu()
    def balance(self):
        print("The balance is "+str(self.__accounts[self.user]))
        return
    def withdrawl(self):
        take = eval(input("Enter an amount to withdraw: "))
        self.__accounts[self.user] -= take
        return
    def deposit(self):
        give = eval(input("Enter the amount to deposit: "))
        self.__accounts[self.user] += give
        return

accounts = []
for i in range(10):
    accounts.append(100)
b = Bank(accounts)
b.user()
        
