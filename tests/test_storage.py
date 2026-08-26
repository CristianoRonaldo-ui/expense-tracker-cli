from src.expense_tracker.storage import save_expenses, load_expenses


def test_save_and_load_expenses(tmp_path):
    filepath = tmp_path / "expenses.json"
    expenses = [{"description": "Coffee", "amount": 4.5, "category": "Food"}]

    save_expenses(expenses, filepath=str(filepath))
    loaded = load_expenses(filepath=str(filepath))

    assert loaded == expenses


def test_load_expenses_missing_file(tmp_path):
    filepath = tmp_path / "does_not_exist.json"
    assert load_expenses(filepath=str(filepath)) == []