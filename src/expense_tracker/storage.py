import json


def save_expenses(expenses: list, filepath: str = "data/expenses.json") -> None:
    """Save a list of expense dicts to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent=2)


def load_expenses(filepath: str = "data/expenses.json") -> list:
    """Load the list of expenses from a JSON file. Returns an empty list if it doesn't exist yet."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []