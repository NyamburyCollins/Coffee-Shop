class Customer:
    all = []

    def __init__(self, name):
        self.name = name  # Uses the property setter
        self._orders = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    @property
    def orders(self):
        return self._orders

    @property
    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from lib.order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        max_total = 0.0
        aficionado = None
        
        for customer in cls.all:
            total = sum(
                order.price 
                for order in customer.orders 
                if order.coffee == coffee
            )
            
            if total > max_total:
                max_total = total
                aficionado = customer  # Track the customer with highest total
                
        return aficionado if max_total > 0 else None  # Return None if no orders