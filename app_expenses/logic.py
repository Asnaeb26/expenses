def get_income(data: dict, user) -> dict:
    return {
        'created': data.get('created'),
        'amount': data.get('amount'),
        'category': data.get('category'),
        'user': user.id
    }


def get_expenses(expenses: list, user) -> list:
    for expense in expenses:
        expense['user'] = user.id
    return expenses
