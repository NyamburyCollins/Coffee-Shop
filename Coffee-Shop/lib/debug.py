# debug_coffee_shop.py
from termcolor import colored
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def print_header(text):
    print(colored(f"\n=== {text} ===", "blue", attrs=["bold"]))

def debug_session():
    print_header("Initializing Debug Session")
    
    # Create sample data
    try:
        # Create customers
        alice = Customer("Alice")
        bob = Customer("Bob")
        eve = Customer("Eve")

        # Create coffees
        latte = Coffee("Latte")
        cappuccino = Coffee("Cappuccino")
        americano = Coffee("Americano")

        # Create orders
        order1 = Order(alice, latte, 4.5)
        order2 = Order(bob, cappuccino, 5.0)
        order3 = Order(eve, americano, 3.75)
        order4 = Order(alice, cappuccino, 5.25)

        print(colored("✓ Sample data created successfully", "green"))
    except Exception as e:
        print(colored(f"Data creation failed: {str(e)}", "red"))
        return

    print_header("Testing Relationships")
    
    # Test customer-coffee relationships
    try:
        print(colored("\nAlice's Orders:", "yellow"))
        for order in alice.orders:
            print(f"- {order.coffee.name}: ${order.price:.2f}")

        print(colored("\nCappuccino Orders:", "yellow"))
        for order in cappuccino.orders:
            print(f"- {order.customer.name}: ${order.price:.2f}")

        print(colored("\nAlice's Coffees:", "yellow"))
        unique_coffees = {order.coffee.name for order in alice.orders}
        for coffee in unique_coffees:
            print(f"- {coffee}")

    except Exception as e:
        print(colored(f"Relationship test failed: {str(e)}", "red"))

    print_header("Testing Advanced Functionality")
    
    # Test if methods exist
    try:
        print("Coffee prices:")
        print(f"Latte average price: ${latte.average_price():.2f}")
        print(f"Top customer for Cappuccino: {cappuccino.top_customer().name}")
        print(f"Eve's total spent: ${eve.total_spent():.2f}")
    except Exception as e:
        print(colored(f"Advanced method test failed: {str(e)}", "red"))

    print_header("Interactive Mode")
    while True:
        try:
            command = input(colored("\nEnter command (help for options): ", "cyan")).strip().lower()
            
            if command == "exit":
                print(colored("Exiting debug session...", "magenta"))
                break
                
            elif command == "help":
                print(colored("Commands:", "green"))
                print("- create customer [name]")
                print("- create coffee [name]")
                print("- place order [customer] [coffee] [price]")
                print("- list customers")
                print("- list coffees")
                print("- inspect [customer/coffee] [name]")
                print("- exit")
                
            elif command.startswith("create customer"):
                name = command.split(" ", 2)[2]
                globals()[name.lower()] = Customer(name)
                print(colored(f"Created customer: {name}", "green"))
                
            elif command.startswith("create coffee"):
                name = command.split(" ", 2)[2]
                globals()[name.lower()] = Coffee(name)
                print(colored(f"Created coffee: {name}", "green"))
                
            elif command.startswith("place order"):
                _, _, customer, coffee, price = command.split(" ", 4)
                Order(globals()[customer.lower()], globals()[coffee.lower()], float(price))
                print(colored(f"Order placed: {customer} bought {coffee} for ${price}", "green"))
                
            elif command == "list customers":
                print(colored("\nCustomers:", "yellow"))
                for var in globals().values():
                    if isinstance(var, Customer):
                        print(f"- {var.name}")
                        
            elif command == "list coffees":
                print(colored("\nCoffees:", "yellow"))
                for var in globals().values():
                    if isinstance(var, Coffee):
                        print(f"- {var.name}")
                        
            elif command.startswith("inspect"):
                _, obj_type, name = command.split(" ", 2)
                obj = globals()[name.lower()]
                
                if isinstance(obj, Customer):
                    print(colored(f"\nInspecting Customer: {obj.name}", "yellow"))
                    print(f"Total orders: {len(obj.orders)}")
                    print(f"Unique coffees: {len(obj.coffees)}")
                    if hasattr(obj, "total_spent"):
                        print(f"Total spent: ${obj.total_spent():.2f}")
                        
                elif isinstance(obj, Coffee):
                    print(colored(f"\nInspecting Coffee: {obj.name}", "yellow"))
                    print(f"Total orders: {len(obj.orders)}")
                    print(f"Average price: ${obj.average_price():.2f}")
                    if hasattr(obj, "top_customer"):
                        top = obj.top_customer()
                        print(f"Top customer: {top.name if top else 'None'}")
                        
            else:
                print(colored("Invalid command", "red"))
                
        except Exception as e:
            print(colored(f"Error: {str(e)}", "red"))

if __name__ == "__main__":
    debug_session()