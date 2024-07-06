# SauceDemo Automated Testing

This project contains automated tests for the SauceDemo website using Python, Selenium, and Pytest.

## Scenarios Covered
1. Successful Login
2. Failed Login
3. Ordering a Product


## Run tests
1. For Valid Successful Login 
    # pytest -s -v test_cases/test_login_home_page.py 
2. For Valid Ordering a Product
   # pytest -s -v test_cases/test_order.py

## For installing upgrades packages
    pip install -r requirements.txt

## For Generating HTML report
    install 'pytest-html' plugin
    
    # Run test with html report generation
        pytest --html=report.html





