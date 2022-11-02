from budget import Budget


with open("food.txt", "r") as file1:
    amount = int(file1.read())

food = Budget(amount)
print(food.balance)
food.withdraw(50)
with open("food.txt", "w") as file1:
    file1.write(str(food.balance))

print(food.balance)