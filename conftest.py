import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.8.140")
    parser.addoption("--prod", action="store", default="http://demo.opencart.com")
    parser.addoption("--stage", action="store", choices=["branch", "staging"], default="branch")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    base_url = request.config.getoption("--prod")
    reference_url = "https://konflic.github.io/front_example/{}.html".format(request.config.getoption("--stage"))

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        # "screenResolution": "1280x720",
        "name": "Mikhail",
        'acceptSslCerts': True,
        "selenoid:options": {
            "enableVNC": True
        },
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    driver.reference_url = reference_url
    driver.base_url = base_url

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
