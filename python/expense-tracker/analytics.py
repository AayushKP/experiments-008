def category_summary(expenses: list[dict]) -> dict:
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense.get("amount", 0)
        summary[category] = amount + summary.get(category, 0)

    return summary
