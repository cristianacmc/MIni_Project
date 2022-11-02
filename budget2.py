from budget import Budget


with open("food.txt", "r") as file1:
    amount = int(file1.read())
food = Budget(amount)

with open("bills.txt", "r") as file1:
    amount = int(file1.read())
bill = Budget(amount)

control = True
while control:
    print("Menu: click 1 for option a or 2 for option b: ")
    input1 = int(input("Please enter your choice: "))

    if input1 == 1:
        amount = int(input("How much would you like to deposit? "))
        food.deposit(amount) 
        with open("food.txt", "w") as f:
            f.write(str(food.balance))
        print("Current balance: ", food.balance)
    elif input1 == 2:
        amount = int(input("How much would you like to withdraw? "))
        food.withdraw(amount) 
        with open("food.txt", "w") as f:
            f.write(str(food.balance))
        print("Current balance: ", food.balance)
    elif input1 == 0:
        control = False 
    else:
        print("Invalid option")

