import os
import allure
import pytest

from config import TMP_FOLDER
from screenshots.helpers import compare_images_hard


@pytest.mark.parametrize("screen", ["640x480", "1024x768", "1280x720"])
@allure.title("Comparing pages with rectangles: {screen}")
def test_main_page_scaling(browser, screen):
    browser.set_window_size(*screen.split("x"))

    mark = browser.session_id[:5]
    master_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    staging_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))

    browser.get(browser.base_url)
    browser.save_screenshot(master_path)

    browser.get(browser.reference_url)
    browser.save_screenshot(staging_path)

    compare_images_hard(master_path, staging_path)