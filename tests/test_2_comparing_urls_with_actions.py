import os
import allure

from config import TMP_FOLDER
from screenshots.helpers import comparison_test_light


@allure.title("Comparing pages test with basic")
def test_interactive_element(browser):
    mark = browser.session_id[:5]

    prod_screenshot_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    stag_screenshot_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))
    diff_screenshot_path = os.path.join(TMP_FOLDER, "{}_diff.png".format(mark))

    for url, scr in [
        (browser.base_url, prod_screenshot_path),
        (browser.reference_url, stag_screenshot_path)
    ]:
        browser.get(url)
        browser.find_element_by_id("form-currency").click()
        browser.save_screenshot(scr)

    comparison_test_light(prod_screenshot_path, stag_screenshot_path, diff_screenshot_path)
