class MoneyAction:

    def __init__(self, data, category_id):
        self.created = data.get('created')
        self.amount = data.get('amount')
        self.currency = data.get('currency')
        self.category_id = category_id

    def create_data(self):
        return {
            'created': self.created,
            'amount': self.amount,
            'currency': self.currency,
            'category_id': self.category_id
        }
