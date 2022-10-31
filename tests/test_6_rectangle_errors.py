import allure

from screenshots.helpers import compare_images_hard, make_tmp_file_path


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with rectangle diff")
def test_main_page_rectangles(browser):
    master_path = make_tmp_file_path(browser, "prod")
    staging_path = make_tmp_file_path(browser, "staging")

    browser.get(browser.prod_url)
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    compare_images_hard(master_path, staging_path)
