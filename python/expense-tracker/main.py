from analytics import category_summary, monthly_summary
from storage import load_expenses, save_expenses

expenses: list[dict] = load_expenses()


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
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def view_expenses() -> None:
    print()

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 75)
    print(f"{'Category':<15}{'Amount':<12}{'Date':<15}Description")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['date']:<15}"
            f"{expense['description']}"
        )

    print("-" * 75)


def add_expense() -> None:
    amount = get_amount()

    category = input("Enter category: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    description = input("Enter description: ").strip()

    expense = create_expense(
        amount,
        category,
        date,
        description,
    )

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")


def main() -> None:
    while True:
        print("\n========== Expense Tracker ==========")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_expenses()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            summary = category_summary(expenses)

            if not summary:
                print("No expenses found.")

            else:
                print("\nCategory Summary")
                print("-" * 30)

                for category, total in summary.items():
                    print(f"{category:<15} ₹{total}")

                print()

        elif choice == "4":
            summary = monthly_summary(expenses)

            if not summary:
                print("No expenses found.")
            else:
                print("\nMonthly Summary")
                print("-" * 30)

                for month, total in summary.items():
                    print(f"{month:<15} ₹{total}")

                print()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
