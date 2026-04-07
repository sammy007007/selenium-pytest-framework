## Key Features
Page Object Model (POM)
Improves maintainability by separating test logic from page interactions.
Pytest Framework
Uses fixtures for setup/teardown and supports scalable test execution.
Explicit Waits (No Hardcoded Sleeps)
Ensures stable and reliable test execution for dynamic web elements.
Reusable BasePage
Common Selenium actions (click, type, wait) are centralized.
HTML Reporting
Generates detailed execution reports using pytest-html.

## Project Structure
*   `pages/` - Contains page classes and element locators.
*   `tests/` - Contains the test scripts (e.g., `test_login.py`).
*   `conftest.py` - Global fixtures and driver configuration.
*   `requirements.txt` - Project dependencies.



### Prerequisites
*   Python 3.10+
*   Chrome or Firefox Browser

### Installation
1. Clone the repository:
   `git clone https://github.com`
2. Install dependencies:
   `pip install -r requirements.txt`

### Running Tests
To execute all tests and generate a report, run the command below by replacing  placeholder `<password>` with  actual password:
```bash
pytest --password=<password>


