from src.expense_tracker.models import create_expense
from src.expense_tracker.storage import load_expenses, save_expenses


def add_expense(description: str, amount: float, category: str) -> dict:
    """Create a new expense, append it to storage, and return it"""
    expense = create_expense(description, amount, category)
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return expense

def get_summary(expenses: list) -> dict:
    """Return total amount spent per category"""
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount
    return summary

def delete_expense(index: int) -> dict:
    """Remove the expense at the given index and return it."""
    expenses = load_expenses()
    removed = expenses.pop(index)
    save_expenses(expenses)
    return removed