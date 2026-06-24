income_list = []
expense_list = []

# Load income data 
try:
    with open("income.txt", "r") as file:
        for line in file:
            source, amount = line.strip().split(",")

            income_list.append({
                "source": source,
                "amount": float(amount)
            })
except FileNotFoundError:
    pass

# Load expense data
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            source, category, amount = line.strip().split(",")

            expense_list.append({
                "source": source,
                "category": category,
                "amount": float(amount)
            })
except FileNotFoundError:
    pass

while True:
    print("\n===== Personal Finance Tracker =====")
    print("1. Add Income")
    print("2. View Income")
    print("3. Add Expense")
    print("4. View Expenses")
    print("5. Calculate Balance")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        source = input("Income Source: ")
        amount = float(input("Amount: "))

        income = {
            "source": source,
            "amount": amount
        }

        income_list.append(income)

        with open("income.txt", "a") as file:
            file.write(f"{source},{amount}\n")

        print("Income added successfully!")

    elif choice == "2":
        print("\nIncome Records:")

        if not income_list:
            print("No income records found.")
        else:
            for income in income_list:
                print(f"- {income['source']} - ${income['amount']}")

    elif choice == "3":
        source = input("Expense Name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))

        expense = {
            "source": source,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

        with open("expenses.txt", "a") as file:
            file.write(f"{source},{category},{amount}\n")

        print("Expense added successfully!")

    elif choice == "4":
        print("\nExpense Records:")

        if not expense_list:
            print("No expense records found.")
        else:
            for expense in expense_list:
                print(
                    f"- {expense['source']} | "
                    f"{expense['category']} | "
                    f"${expense['amount']}"
                )

    elif choice == "5":
        total_income = sum(income["amount"] for income in income_list)
        total_expenses = sum(expense["amount"] for expense in expense_list)

        balance = total_income - total_expenses

        print("\n===== Financial Summary =====")
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Balance: ${balance}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
