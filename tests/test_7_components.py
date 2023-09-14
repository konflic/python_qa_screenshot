import allure
import pytest
from selenium.webdriver.common.by import By

from screenshots.helpers import make_tmp_file_path, comparison_test_light


@allure.label("testType", "screenshotDiff")
@pytest.mark.parametrize("locator", ["#menu", "#top", "#search", "footer"])
@allure.title("Comparing elements of the page: {locator}")
def test_main_page_elements(browser, locator):
    master_path = make_tmp_file_path(browser, "prod")
    staging_path = make_tmp_file_path(browser, "staging")
    difference = make_tmp_file_path(browser, "diff")
    browser.get(browser.prod_url)
    browser.find_element(By.CSS_SELECTOR, locator).screenshot(master_path)
    browser.get(browser.stag_url)
    browser.find_element(By.CSS_SELECTOR, locator).screenshot(staging_path)
    comparison_test_light(master_path, staging_path, difference, clear_images=False)
