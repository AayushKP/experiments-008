def category_summary(expenses: list[dict]) -> dict:
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense.get("amount", 0)
        summary[category] = amount + summary.get(category, 0)

    return summary


def monthly_summary(expenses: list[dict]) -> dict:
    summary = {}
    for expense in expenses:
        month = expense["date"][:7]
        amount = expense.get("amount", 0)
        summary[month] = amount + summary.get(month, 0)
    return summary
