# Python Playwright Automation Tests

Automated testing framework using Python and Playwright for end-to-end web application testing.

## 📋 Project Overview

This project contains automated tests for web application testing using the Playwright testing library. It follows the **Page Object Model (POM)** design pattern for better code organization and maintainability.

## 🛠️ Technologies Used

- **Python** 3.x
- **Playwright** - Cross-browser automation library
- **Pytest** - Testing framework
- **Page Object Model** - Design pattern for test organization

## 📁 Project Structure

```
Python_playwright/
├── Pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base class for all pages
│   ├── login_page.py          # Login page object
│   ├── checkout_page.py       # Checkout page object
│   ├── inventory_page.py      # Inventory/Products page object
│   └── conftest.py            # Shared fixtures
│
├── tests/                      # Test files
│   ├── conftest.py            # Test configuration and fixtures
│   ├── test_login.py          # Login tests
│   ├── test_inventory_page.py # Inventory tests
│   └── screenshot/            # Test screenshots and results
│
├── pytest.ini                 # Pytest configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone 
   cd Python_playwright
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pytest playwright
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## ▶️ Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests in a Specific File
```bash
pytest tests/test_login.py
```

### Run Tests with Specific Marker
```bash
pytest -m "login"
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Tests in Headed Mode (see browser)
```bash
pytest --headed
```

### Run with Screenshots on Failure
```bash
pytest --screenshot=only-on-failure
```

## 📝 Test Files Description

### **test_login.py**
- Tests for user login functionality
- Validates login with valid/invalid credentials
- Tests session management

### **test_inventory_page.py**
- Tests for inventory/products page
- Product listing verification
- Product filtering and sorting

### **test_checkout.py**
- Checkout flow tests
- Cart management
- Order confirmation

## 🏗️ Page Object Model Structure

Each page class inherits from `BasePage` and contains:
- **Locators**: Element selectors (XPath, CSS selectors, etc.)
- **Methods**: User actions (click, fill, submit, etc.)
- **Assertions**: Verification methods

### Example Usage
```python
from Pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("username", "password")
    assert login_page.is_dashboard_displayed()
```

## ✅ Configuration

### pytest.ini
Contains Pytest configuration like:
- Test discovery patterns
- Output format
- Logging settings
- Browser options

### conftest.py
Shared fixtures and setup:
- Browser initialization
- Page fixtures
- Test data
- Teardown procedures

## 📊 Test Results

Test results and screenshots are stored in:
- `tests/screenshot/` - Screenshots from test runs
- Console output - Detailed test logs

## 🐛 Debugging

### Enable Debug Mode
```bash
pytest --debug
```

### Generate HTML Report
```bash
pytest --html=report.html
```

### View Test Execution
Use `--headed` flag to see the browser during test execution:
```bash
pytest --headed
```

## 📦 Dependencies

- `playwright>=1.40.0` - Browser automation
- `pytest>=7.0.0` - Testing framework
- `pytest-playwright>=0.4.0` - Pytest plugin for Playwright

Install all at once:
```bash
pip install -r requirements.txt
```

## 🔄 Git Workflow

### Committing Changes
```bash
git add .
git commit -m "Descriptive message"
git push origin main
```

### .gitignore Rules
This project ignores:
- `__pycache__/` - Python cache
- `.pytest_cache/` - Pytest cache
- `venv/` - Virtual environment
- `.env` - Environment variables
- IDE settings (`.vscode/`, `.idea/`)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure everything passes
4. Commit and push to GitHub
5. Create a Pull Request

## 📧 Contact & Support

For questions or issues, please open a GitHub issue.

---

**Happy Testing! 🎉**
