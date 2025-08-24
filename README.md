# selenium-python-automationexercise
Selenium Web Automation Framework (Python + Pytest) for automationexercise.com with POM, HTML Reports, CI/CD

## Features
- Page Object Model (POM) implementation
- Data-driven testing using JSON test data
- Configurable test environment
- Reusable utilities and helper functions
- Detailed HTML test reports
- Screenshot capture on test failure
- Clean and maintainable test structure

## Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Git

## Project Structure
```
selenium-python-automationexercise/
├── pages/                  # Page Object Model classes
│   ├── home_page.py       # Home page elements and actions
│   └── login_page.py      # Login page elements and actions
├── test_data/             # Test data files
│   ├── test_users.json    # User credentials (not in git)
│   └── test_users.template.json  # Template for user credentials
├── tests/                 # Test cases
│   └── test_login.py      # Login functionality tests
├── utils/                 # Utility functions
│   └── webdriver_utils.py # WebDriver helper functions
├── reports/              # Test execution reports
├── conftest.py          # Pytest configurations
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/Gaurav-jagtap017/selenium-python-automationexercise.git
cd selenium-python-automationexercise
```

2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up test credentials
```bash
# Copy the template file
cp test_data/test_users.template.json test_data/test_users.json
# Edit test_data/test_users.json with your credentials
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_login.py
```

### Run tests with HTML report
```bash
pytest --html=reports/report.html
```

## Test Data Configuration

The project uses JSON files for test data management. To configure test users:

1. Copy the template:
```bash
cp test_data/test_users.template.json test_data/test_users.json
```

2. Edit `test_users.json` with your test credentials:
```json
{
    "valid_user": {
        "Email": "your_email@example.com",
        "Password": "your_password"
    }
}
```

## Best Practices
- Keep test data separate from test logic
- Use Page Object Model for better maintenance
- Implement explicit waits instead of time.sleep()
- Take screenshots on test failures
- Use meaningful test and variable names
- Add comments for complex operations
- Keep tests independent and atomic

## Common Issues and Solutions

### ChromeDriver Issues
If you encounter ChromeDriver compatibility issues:
1. Check your Chrome browser version
2. Download matching ChromeDriver version
3. Add ChromeDriver to system PATH

### Test Data Issues
- Ensure `test_users.json` is properly configured
- Check file permissions
- Verify JSON syntax

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Python Documentation](https://docs.python.org/)
- [Automation Exercise Website](https://automationexercise.com/)
