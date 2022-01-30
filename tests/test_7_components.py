import allure
import pytest

from screenshots.helpers import compare_images_hard, make_tmp_file


@pytest.mark.parametrize("locator", ["#menu", "#top", "#cart", "#slideshow0", ".product-thumb", "#carousel0"])
@allure.title("Comparing elements of the page: {locator}")
def test_main_page_elements(browser, locator):
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")

    browser.get(browser.prod_url)
    browser.find_element_by_css_selector(locator).screenshot(master_path)

    browser.get(browser.stag_url)
    browser.find_element_by_css_selector(locator).screenshot(staging_path)

    compare_images_hard(master_path, staging_path)
