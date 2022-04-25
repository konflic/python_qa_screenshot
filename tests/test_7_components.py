import allure
import pytest

from screenshots.helpers import make_tmp_file, comparison_test_light


@pytest.mark.parametrize("locator", ["#menu", "#top", "#search", "footer"])
@allure.title("Comparing elements of the page: {locator}")
def test_main_page_elements(browser, locator):
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")
    difference = make_tmp_file(browser, "diff")

    browser.get(browser.prod_url)
    browser.find_element_by_css_selector(locator).screenshot(master_path)

    browser.get(browser.stag_url)
    browser.find_element_by_css_selector(locator).screenshot(staging_path)

    comparison_test_light(master_path, staging_path, difference, clear_images=False)
