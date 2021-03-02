import os
import allure

from config import TMP_FOLDER
from screenshots.helpers import compare_images_hard


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with rectangle diff")
def test_main_page_rectangles(browser):
    mark = browser.session_id[:5]

    master_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    staging_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))

    browser.get(browser.base_url)
    browser.save_screenshot(master_path)

    browser.get(browser.reference_url)
    browser.save_screenshot(staging_path)

    compare_images_hard(master_path, staging_path)
