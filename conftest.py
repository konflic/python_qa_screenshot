import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mobile", action="store_true", help="test mobile emulation")
    parser.addoption("--prod", action="store", default="http://demo.opencart.com")
    parser.addoption("--stage", action="store", choices=["branch", "staging"], default="branch")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    mobile = request.config.getoption("--mobile")
    prod_url = request.config.getoption("--prod")
    stag_url = "https://konflic.github.io/front_example/{}.html".format(request.config.getoption("--stage"))

    caps = {
        "browserName": browser,
        "browserVersion": "91.0" if browser == "chrome" else "",
        "screenResolution": "1920x1080",
        "name": "Mikhail",
        "selenoid:options": {
            "enableVNC": True
        },
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {}
    }

    if browser == "chrome" and mobile:
        caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    driver = webdriver.Remote(
        command_executor="http://192.168.1.79:4444/wd/hub",
        desired_capabilities=caps
    )

    driver.stag_url = stag_url
    driver.prod_url = prod_url

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
