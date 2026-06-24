income_list = []

while True:
    print("\n===== Personal Finance Tracker =====")
    print("1. Add Income")
    print("2. View Income")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        source = input("Income Source: ")
        amount = float(input("Amount: "))

        income = f"{source} - ${amount}"

        income_list.append(income)

        print("Income added successfully!")

    elif choice == "2":
        print("\nIncome Records:")

        if not income_list:
            print("No income records found.")
        else:
            for income in income_list:
                print("-", income)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
