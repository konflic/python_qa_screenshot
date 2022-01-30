import allure

from screenshots.helpers import comparison_test_light, make_tmp_file


@allure.title("Comparing pages test with basic comparison")
def test_main_page(browser):
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")
    diff_path = make_tmp_file(browser, "diff")

    browser.get(browser.prod_url)
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    comparison_test_light(master_path, staging_path, diff_path, clear_images=False)
