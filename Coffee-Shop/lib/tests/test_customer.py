import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

@pytest.fixture
def customer():
    return Customer("Alice")

@pytest.fixture
def coffee():
    return Coffee("Latte")

def test_customer_initialization(customer):
    assert customer.name == "Alice"

def test_invalid_name():
    with pytest.raises(ValueError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLongForValidation")

def test_orders_property(customer, coffee):
    order = Order(customer, coffee, 5.0)
    assert len(customer.orders) == 1  # ✅ Fixed: No ()
    assert order in customer.orders   # ✅ Fixed: No ()

def test_coffees_property(customer, coffee):
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 5.0)
    assert len(customer.coffees) == 1  # ✅ Fixed: No ()
    assert coffee in customer.coffees  # ✅ Fixed: No ()

def test_create_order(customer, coffee):
    order = customer.create_order(coffee, 6.0)
    assert order in customer.orders   # ✅ Fixed: No ()
    assert order in coffee.orders     # ✅ Fixed: No ()

def test_most_aficionado(coffee):
    Customer.all.clear()
    c1 = Customer("Bob")
    c2 = Customer("Charlie")
    
    Order(c1, coffee, 4.0)
    Order(c1, coffee, 5.0)
    Order(c2, coffee, 10.0)
    
    assert Customer.most_aficionado(coffee).name == "Charlie"

def test_most_aficionado_no_orders(coffee):
    Customer.all.clear()
    assert Customer.most_aficionado(coffee) is None