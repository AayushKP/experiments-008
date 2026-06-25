import json

FILE_NAME = "expenses.json"


def save_expenses(expenses: list[dict]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)


def load_expenses() -> list[dict]:
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
