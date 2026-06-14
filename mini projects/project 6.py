accounts =[]

def create_account(name, balance):
    account = {"name": name, "balance": balance}
    accounts.append(account)
    print("account created successfully")
def show_accounts():
    if len(accounts) == 0:
        print("no accounts found")
    else:
        for a in accounts:
            print(a["name"], "-", a["balance"])
def deposit():
    name = input("enter account name:")
    amount = float(input("enter deposit amount:"))
    for a in accounts:
        if a["name"] == name:
            a["balance"] += amount
            print("deposit successful")
            return
    print("account not found")
def withdraw():
    name = input("enter account name:")
    amount = float(input("enter withdrawal amount:"))
    for a in accounts:
        if a["name"] == name:
            if a["balance"] >= amount:
                a["balance"] -= amount
                print("withdrawal successful")
            else:
                print("insufficient balance")
            return
    print("account not found")
while True:
    print("\n1. Create Account")
    print("2. Show Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("enter account name:")
        balance = float(input("enter initial balance:"))
        create_account(name, balance)

    elif choice == "2":
        show_accounts()

    elif choice == "3":
        deposit()

    elif choice == "4":
        withdraw()

    elif choice == "5":
        break

    else:
        print("Invalid choice")                        