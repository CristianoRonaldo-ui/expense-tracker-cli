# Expense Tracker CLI

A simple command-line tool for tracking personal expenses. Add expenses, list them, see spending totals by category, and delete entries — all from the terminal.

## Features

- Add an expense with a description, amount, and category
- List all recorded expenses
- View total spending grouped by category
- Delete an expense by its position in the list
- Data is stored locally in a JSON file (`data/expenses.json`)

## Project Structure
expense-tracker-cli/
├── src/expense_tracker/
│ ├── models.py # Expense creation and validation
│ ├── storage.py # Read/write expenses to a JSON file
│ ├── operations.py # Business logic: add, summarize, delete
│ └── cli.py # Command-line interface (argparse)
├── tests/ # pytest test suite
└── data/ # generated expenses.json (not tracked in git)

## Setup

```bash
git clone https://github.com/CristianoRonaldo-ui/expense-tracker-cli.git
cd expense-tracker-cli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Add an expense
python3 -m src.expense_tracker.cli add "Coffee" 4.5 Food

# List all expenses
python3 -m src.expense_tracker.cli list

# Show total spending per category
python3 -m src.expense_tracker.cli summary

# Delete an expense by its index (from `list`)
python3 -m src.expense_tracker.cli delete 0
```

### Example

$ python3 -m src.expense_tracker.cli add "Coffee" 4.5 Food
Added: {'description': 'Coffee', 'amount': 4.5, 'category': 'Food'}

$ python3 -m src.expense_tracker.cli add "Bus ticket" 3.25 Transport
Added: {'description': 'Bus ticket', 'amount': 3.25, 'category': 'Transport'}

$ python3 -m src.expense_tracker.cli list
0: Coffee - $4.50 (Food)
1: Bus ticket - $3.25 (Transport)

$ python3 -m src.expense_tracker.cli summary
Food: $4.50
Transport: $3.25


## Complexity

- Adding an expense: O(n) — reads and rewrites the full JSON file (n = number of expenses).
- Listing expenses: O(n).
- Summary by category: O(n) — one pass through the list, using a dictionary to accumulate totals.
- Deleting by index: O(n) — due to `list.pop(index)` shifting elements, plus the file rewrite.

## What I Learned

- Structuring a small Python project into separate modules (models, storage, business logic, CLI) instead of one script.
- Using `argparse` with subcommands to build a real command-line interface.
- Reading and writing JSON files with Python's `json` module.
- Writing pure, testable functions (like `get_summary`) that don't depend on files or user input.