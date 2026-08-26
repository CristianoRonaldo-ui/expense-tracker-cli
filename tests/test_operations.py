from src.expense_tracker.operations import get_summary


def test_get_summary_groups_by_category():
    expenses = [
        {"description": "Coffee", "amount": 4.5, "category": "Food"},
        {"description": "Lunch", "amount": 10.0, "category": "Food"},
        {"description": "Bus ticket", "amount": 3.25, "category": "Transport"},
    ]

    summary = get_summary(expenses)

    assert summary == {"Food": 14.5, "Transport": 3.25}


def test_get_summary_empty_list():
    assert get_summary([]) == {}