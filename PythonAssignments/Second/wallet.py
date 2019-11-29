def wallet(open):
    balance = open

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        print("Your balance", balance)

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("Not enough balance")
            return False
        else:
            print("Final balance after withdrawing", amount)
            balance = balance - amount
            print("Your balance", balance)
            return True

    def showbalance():
        nonlocal balance
        print("Your account balance", balance)

    return {"deposit": deposit, "withdraw": withdraw, "showbalance": showbalance}


def transfer(w1, amount, w2):
    if w1["withdraw"](amount):
        w2["deposit"](amount)


wallet1 = wallet(500)
wallet2 = wallet(2000)


print("Wallet 1 functions started", end="\n\n")
wallet1["deposit"](100)
wallet1["withdraw"](1000)
wallet1["withdraw"](200)
wallet1["showbalance"]()

print("Wallet 1 functions completed", end="\n\n")

print("Wallet 2 functions started", end="\n\n")
wallet2["deposit"](100)
wallet2["withdraw"](1000)
wallet2["withdraw"](200)
wallet2["showbalance"]
print("Wallet 2 functions completed", end="\n\n")

print("Transfer Start")
transfer(wallet1, 200, wallet2)
