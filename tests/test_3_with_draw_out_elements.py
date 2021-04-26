import os
import time
import allure

from config import TMP_FOLDER
from screenshots.helpers import comparison_test_light_with_draw


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with draw elements out")
def test_main_page_draw_elements_out(browser):
    mark = browser.session_id[:5]

    master_path = os.path.join(TMP_FOLDER, "{}_prog.png".format(mark))
    staging_path = os.path.join(TMP_FOLDER, "{}_stag.png".format(mark))
    diff_path = os.path.join(TMP_FOLDER, "{}_diff.png".format(mark))

    browser.get(browser.prod_url)
    time.sleep(3.5)  # We want slider swipe
    slider_dim = browser.find_element_by_css_selector("#slideshow0").rect
    slider_pag_dim = browser.find_element_by_css_selector(".swiper-pagination").rect
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    comparison_test_light_with_draw(
        master_path,
        staging_path,
        diff_path,
        draw_out=[slider_dim, slider_pag_dim],
        clear_images=False
    )
