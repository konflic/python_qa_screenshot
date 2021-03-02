import os
import time
import allure

from config import TMP_FOLDER
from screenshots.helpers import comparison_test_light_with_draw


@allure.title("Comparing pages test with basic")
def test_main_page_remove_elements(browser):
    mark = browser.session_id[:5]

    master_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    staging_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))
    diff_path = os.path.join(TMP_FOLDER, "{}_diff.png".format(mark))
    
    def remove_elements(driver, selectors: list):
        for selector in selectors:
            browser.execute_script("$('{}')[0].remove()".format(selector))

    browser.get(browser.base_url)
    time.sleep(3.5)  # We want slider swipe
    remove_elements(browser, ["#slideshow0", ".swiper-pagination"])
    browser.save_screenshot(master_path)

    browser.get(browser.reference_url)
    remove_elements(browser, ["#slideshow0", ".swiper-pagination"])
    browser.save_screenshot(staging_path)

    comparison_test_light_with_draw(
        master_path,
        staging_path,
        diff_path,
        clear_images=False
    )
