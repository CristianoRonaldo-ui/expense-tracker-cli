import argparse

from src.expense_tracker.operations import add_expense, get_summary, delete_expense
from src.expense_tracker.storage import load_expenses

def main() -> None:
    parser = argparse.ArgumentParser(description="A simple command-line expense tracker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category", type=str)
    summary_parser = subparsers.add_parser("summary", help="Show total spending by category")
    list_parser = subparsers.add_parser("list", help="List all expenses")
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by its index")
    delete_parser.add_argument("index", type=int)

    args = parser.parse_args()

    if args.command == "add":
        expense = add_expense(args.description, args.amount, args.category)
        print(f"Added: {expense}")
    elif args.command == "summary":
        summary = get_summary(load_expenses())
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    elif args.command == "list":
        expenses = load_expenses()
        if not expenses:
            print("No expenses recorded yet.")
        for i, expense in enumerate(expenses):
            print(f"{i}: {expense['description']} - ${expense['amount']:.2f} ({expense['category']})")
    elif args.command == "delete":
        removed = delete_expense(args.index)
        print(f"Deleted: {removed}")


if __name__ == "__main__":
    main()