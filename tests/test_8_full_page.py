import allure

from screenshots.helpers import compare_images_hard, make_tmp_file


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with rectangle diff")
def test_main_page_rectangles(browser):
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")

    browser.get(browser.prod_url)
    browser.get_full_page_screenshot_as_file(master_path)

    browser.get(browser.stag_url)
    browser.get_full_page_screenshot_as_file(staging_path)

    compare_images_hard(master_path, staging_path, clear_image=False)
