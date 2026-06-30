from analytics import category_summary, monthly_summary
from expense import Expense
from storage import load_expenses, save_expenses

expenses = load_expenses()


def create_expense(
    amount: float, category: str, date: str, description: str
) -> Expense:
    return Expense(amount=amount, category=category, date=date, description=description)


def get_amount() -> float:
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive")
                continue
            return amount
        except ValueError:
            print("Invalid amount")


def add_expense():
    amount = get_amount()
    category = input("Category: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    description = input("Description: ").strip()

    expense = create_expense(amount, category, date, description)
    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added!")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print()
    print("-" * 75)
    print(f"{'Category':<15}{'Amount':<12}{'Date':<15}Description")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense.category:<15}"
            f"₹{expense.amount:<11.2f}"
            f"{expense.date:<15}"
            f"{expense.description}"
        )

    print()


def show_category_summary():
    summary = category_summary(expenses)

    if not summary:
        print("\nNo expenses found.")
        return

    print("Category Summary")
    print("-" * 30)

    for category, total in summary.items():
        print(f"{category:<15}₹{total}")

    print()


def show_monthly_summary():
    summary = monthly_summary(expenses)

    if not summary:
        print("\nNo expenses found.")
        return

    print("Monthly Summary")
    print("-" * 30)

    for month, total in summary.items():
        print(f"{month:<15}₹{total}")

    print()


def main():
    while True:
        print()
        print("Expense Tracker")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            view_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_category_summary()
        elif choice == "4":
            show_monthly_summary()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()
