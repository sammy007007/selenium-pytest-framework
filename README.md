## Key Features
Page Object Model (POM)
I’ve used POM to keep things clean by separating test logic from page-level actions. This makes the framework easier to maintain and scale as per requirements.
Pytest Framework
Using Pytest with fixtures helps manage setup and teardown smoothly and keeps the tests structured.
Explicit Waits (No Hardcoded Sleeps)
No sleep() used — everything is handled with proper waits to make tests stable and reliable.
Reusable BasePage
Common actions like click, type, wait, etc., are centralized to avoid code duplication and follow DNR.
HTML Reporting
Test execution reports are generated using pytest-html for better visibility.

## Project Structure
*   `pages/` - Contains page classes and element locators.
*   `tests/` - Contains the test scripts (e.g., `test_login.py`).
*   `conftest.py` - Handles global fixtures , WebDriver setup and handle login.
*   `utils/driver_factory.py` - Configuration for browser drivers.
*   `requirements.txt` - Project dependencies.
*   `tests` - Currently contain only two sample  testcases : 
               TC001: Validate product search functionality for"snowboard"
               TC002: Validate adding the first displayed product to cart after searching for "snowboard"



### Prerequisites
*   Python 3.10+
*   Chrome Browser
*   Windows OS (tests are developed and verified on Windows)


### Installation
1. Clone the repository:
   `git clone https://github.com`
2. Setup Virtual Environment :
   `python -m venv venv`
   `venv\Scripts\activate`
3. Install dependencies:
   `pip install -r requirements.txt`



### Running Tests
To execute all tests and generate a report, run the command below by replacing  placeholder `<password>` with  actual password:
```bash
pytest --password=<password>


