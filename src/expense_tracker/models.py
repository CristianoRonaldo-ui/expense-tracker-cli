def create_expense(description: str, amount: float, category: str) -> dict:
    """Create and validate a single expense, returned as a dict."""
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if not description.strip():
        raise ValueError("Description cannot be empty")

    return {
        "description": description,
        "amount": amount,
        "category": category,
    }