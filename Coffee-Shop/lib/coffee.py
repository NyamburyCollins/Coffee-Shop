class Coffee:
    def __init__(self, name):
        self.name = name  # Uses the property setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    @property
    def orders(self):
        """List of all orders for this coffee"""
        return self._orders

    @property
    def num_orders(self):
        """Total number of times this coffee has been ordered"""
        return len(self._orders)

    @property
    def customers(self):
        """Unique list of customers who ordered this coffee"""
        return list({order.customer for order in self._orders})

    @property
    def average_price(self):
        """Average price paid for this coffee across all orders"""
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return round(total / len(self._orders), 2)