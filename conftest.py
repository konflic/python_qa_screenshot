import allure
import pytest

from config import BASE_URL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mobile", action="store_true", help="test mobile emulation")
    parser.addoption("--prod", action="store", default=f"{BASE_URL}/prod.html")
    parser.addoption("--stage", action="store", choices=["branch", "staging"], default="staging")
    parser.addoption("--executor", action="store", default="127.0.0.1")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    mobile = request.config.getoption("--mobile")
    prod_url = request.config.getoption("--prod")
    executor = request.config.getoption("--executor")
    stage_url = f"{BASE_URL}/{request.config.getoption('--stage')}.html"

    options = None

    capabilities = {
        "browserName": browser,
        "selenoid:options": {
            "enableVNC": True,
            "timeZone": "Europe/Moscow",
        },
        "goog:chromeOptions": {}
    }

    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FFOptions()

    if mobile:
        options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone XR"})

    for k, v in capabilities.items():
        options.set_capability(k, v)

    if browser == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            options=options
        )

    driver.stag_url, driver.prod_url = stage_url, prod_url

    allure.attach(
        name="config",
        body=f"'stg': {stage_url}\n'prd': {prod_url}",
        attachment_type=allure.attachment_type.TEXT
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
