class Budget():
    def __init__(self, balance ):
        self.balance = balance
    
    def __repr__(self):
        return f"This balance is currently: {self.balance}."

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
        return amount 

food = Budget(500)
with open("food.txt", "w") as f:
    f.write(str(food.balance))

bill = Budget(200)
with open("bills.txt", "w") as f:
    f.write(str(bill.balance))






