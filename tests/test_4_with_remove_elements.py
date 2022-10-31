import time
import allure

from screenshots.helpers import comparison_test_light, make_tmp_file_path


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with basic")
def test_main_page_remove_elements(browser):
    master_path = make_tmp_file_path(browser, "prod")
    staging_path = make_tmp_file_path(browser, "staging")
    diff_path = make_tmp_file_path(browser, "diff")

    def remove_elements(driver, selectors: list):
        for selector in selectors:
            driver.execute_script("$('{}')[0].remove()".format(selector))

    elements = ["#slideshow0", ".swiper-pagination", ".product-thumb .caption"]

    browser.get(browser.prod_url)
    time.sleep(3)  # We want slider swipe
    remove_elements(browser, elements)
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    remove_elements(browser, elements)
    browser.save_screenshot(staging_path)

    comparison_test_light(master_path, staging_path, diff_path, clear_images=False)
