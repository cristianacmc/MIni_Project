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
print(food)
food.withdraw(50)
print(food)
food.deposit(50)
print(food)

with open("food.txt", "w") as f:
    f.write(str(food.balance))


