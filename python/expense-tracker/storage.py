import json
from dataclasses import asdict

from expense import Expense

FILE_NAME = "expenses.json"


def save_expenses(expenses: list[Expense]) -> None:
    data = [asdict(expense) for expense in expenses]
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_expenses() -> list[Expense]:
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Expense(**expense) for expense in data]
    except FileNotFoundError:
        return []
