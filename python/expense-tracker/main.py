expenses = []


def create_expense(
    amount: float,
    category: str,
    date: str,
    description: str,
) -> dict:
    return {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description,
    }


def get_amount() -> float:
    while True:
        try:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be greater than 0")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number")


def view_expenses() -> None:
    print()

    if not expenses:
        print("------- Nothing to show -------")
        return

    print("Expenses:")
    print("-" * 50)

    for expense in expenses:
        print(
            f"{expense['category']} | ₹{expense['amount']} | "
            f"{expense['date']} | {expense['description']}"
        )

    print()


def main() -> None:
    while True:
        print("\nExpense Tracker")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_expenses()

        elif choice == "2":
            amount = get_amount()

            category = input("Enter the category: ").strip()
            date = input("Enter the date (YYYY-MM-DD): ").strip()
            description = input("Enter the description: ").strip()

            expense = create_expense(
                amount,
                category,
                date,
                description,
            )

            expenses.append(expense)

            print("Expense added successfully!")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


main()
