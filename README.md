Python Coffee Shop System

A Python-based system for managing coffee shop operations, including product management, customer orders, and customer relationships.

## Features
- Coffee product management
- Order processing system
- Customer account management
- Comprehensive test coverage
- Type hint support

## Technologies
- **Core**: Python 3.8
- **Testing**: pytest, pytest-mock
- **Documentation**: Python docstrings
- **Packaging**: pip, virtualenv

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/NyamburyCollins/coffee-shop.git
cd python-coffee-shop
Create virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
pipenv install
virtual environment pipenv shell
debug

bash
pip install -r requirements.txt

Project Structure
lib/
  coffee.py       - Coffee product class and inventory management
  customer.py     - Customer data model and management
  order.py        - Order processing and calculations
tests/
  test_*.py       - Unit tests for all modules

Testing
Run all tests with pytest:

bash
pytest -v tests/
Generate coverage report:

bash
pytest --cov=src --cov-report=html

Project Structure
coffee-shop/
├── lib/
│   ├── coffee.py            # Coffee product class and logic
│   ├── order.py             # Order products
│   ├── customer.py          # Customer management
│   └── __init__.py          # Make directory a Python package
├── tests/
│   ├── test_coffee.py       # Tests for coffee module
│   ├── test_order.py        # Tests for order module
│   ├── test_customer.py     # Tests for customer module
│   └── __init__.py          # Test package initialization
├── requirements.txt         # Project dependencies
├── setup.cfg                # Pytest configuration
├── .gitignore
└── README.md

License
MIT License
Collins Nyambury
