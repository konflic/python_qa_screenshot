import os
import allure

from config import TMP_FOLDER
from screenshots.helpers import comparison_test_light


@allure.title("Comparing pages test with basic")
def test_main_page(browser):
    mark = browser.session_id[:5]

    master_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    staging_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))
    diff_path = os.path.join(TMP_FOLDER, "{}_diff.png".format(mark))

    browser.get(browser.prod_url)
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    comparison_test_light(master_path, staging_path, diff_path, clear_images=False)
