import allure
import pytest

from config import BASE_URL
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mobile", action="store_true", help="test mobile emulation")
    parser.addoption("--prod", action="store", default="http://demo.opencart.com")
    parser.addoption("--stage", action="store", choices=["branch", "staging"], default="branch")
    parser.addoption("--executor", action="store", default="192.168.1.82")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    mobile = request.config.getoption("--mobile")
    prod_url = request.config.getoption("--prod")
    executor = request.config.getoption("--executor")
    stag_url = f"{BASE_URL}/{request.config.getoption('--stage')}.html"

    caps = {
        "browserName": browser,
        "screenResolution": "1920x1080",
        "name": "Mikhail",
        "selenoid:options": {
            "enableVNC": True
        },
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {}
    }

    if mobile:
        caps["browserName"] = "chrome"
        caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities=caps
    )

    driver.stag_url, driver.prod_url = stag_url, prod_url

    allure.attach(
        name="config",
        body=f"'stag': {stag_url}\n'prod': {prod_url}",
        attachment_type=allure.attachment_type.TEXT
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
