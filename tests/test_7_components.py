import os
import allure
import pytest

from config import TMP_FOLDER
from screenshots.helpers import compare_images_hard


@pytest.mark.parametrize("locator", ["#menu", "#top", "#cart", "#slideshow0"])
@allure.title("Comparing elements of the page: {locator}")
def test_main_page_elements(browser, locator, screen):
    mark = browser.session_id[:5]
    browser.set_window_size(*screen.split("x"))

    master_path = os.path.join(TMP_FOLDER, "{}_{}_prog.png".format(mark, locator))
    staging_path = os.path.join(TMP_FOLDER, "{}_{}_stag.png".format(mark, locator))

    browser.get(browser.prod_url)
    browser.find_element_by_css_selector(locator).screenshot(master_path)

    browser.get(browser.stag_url)
    browser.find_element_by_css_selector(locator).screenshot(staging_path)

    compare_images_hard(master_path, staging_path)
