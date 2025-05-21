class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None  # ✅ Initialize first
        self._coffee = None    # ✅ Initialize first
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from lib.customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Must be a Customer instance")
        # Remove from old customer
        if self._customer is not None:  # Simplified check
            self._customer.orders.remove(self)
        # Add to new customer
        self._customer = value
        if self not in value.orders:  # Prevent duplicates
            value.orders.append(self)

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from lib.coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        # Remove from old coffee
        if self._coffee is not None:  # Simplified check
            self._coffee.orders.remove(self)
        # Add to new coffee
        self._coffee = value
        if self not in value.orders:  # Prevent duplicates
            value.orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Price must be a number")
        if not 1.0 <= float(value) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)