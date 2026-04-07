## Key Features
*   **Page Object Model (POM):** Enhances test maintenance and reduces code duplication.
*   **Pytest Framework:** Utilizes fixtures for setup and teardown, and parameterization for data-driven testing.
*   **Selenium WebDriver:** Reliable browser automation across Chrome and Firefox.
*   **Custom Reporting:** Integrated with `pytest-html` for detailed execution reports.
*   **Explicit Waits:** Intelligent synchronization to handle dynamic web elements.

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
To execute all tests and generate a report:
```bash
pytest --html=report.html
