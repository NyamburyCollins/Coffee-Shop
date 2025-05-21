import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

@pytest.fixture
def customer():
    return Customer("Ivan")

@pytest.fixture
def coffee():
    return Coffee("Cappuccino")

def test_order_initialization(customer, coffee):
    order = Order(customer, coffee, 8.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 8.0

def test_invalid_customer():
    with pytest.raises(ValueError):
        Order("invalid", Coffee("Test"), 5.0)  # Fails if customer is not a `Customer` instance

def test_invalid_coffee():
    with pytest.raises(ValueError):
        Order(Customer("Test"), "invalid", 5.0)  # Fails if coffee is not a `Coffee` instance

def test_price_validation():
    customer = Customer("Judy")
    coffee = Coffee("Flat White")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Below 1.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Above 10.0
    with pytest.raises(ValueError):
        Order(customer, coffee, "invalid")  # Non-float type

def test_relationship_management(customer, coffee):
    order = Order(customer, coffee, 9.0)
    assert order in customer.orders  # ✅ Fixed: no ()
    assert order in coffee.orders    # ✅ Fixed: no ()

    new_customer = Customer("Kevin")
    order.customer = new_customer
    assert order not in customer.orders  # ✅ Old customer no longer has the order
    assert order in new_customer.orders  # ✅ New customer now has the order