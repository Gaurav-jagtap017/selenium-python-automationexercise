# selenium-python-automationexercise
Selenium Web Automation Framework (Python + Pytest) for automationexercise.com with POM, HTML Reports, CI/CD

# Selenium BDD Framework (Python + Pytest + POM + BDD)

## Tech Stack
- Selenium 4
- Pytest
- Pytest-BDD
- Page Object Model
- Allure Reporting

## Project Structure
- `features/` → Gherkin feature files
- `step_definitions/` → BDD step implementations
- `pages/` → Page Object Model classes
- `utils/` → Driver setup & utilities
- `tests/` → Fixtures & conftest

## How to Run Tests
```bash
pip install -r requirements.txt
pytest --alluredir=reports
allure serve reports
