import allure

from screenshots.helpers import comparison_test_light, make_tmp_file_path


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with basic comparison and actions")
def test_interactive_element(browser):
    prod_screenshot_path = make_tmp_file_path(browser, "prod")
    stag_screenshot_path = make_tmp_file_path(browser, "staging")
    diff_screenshot_path = make_tmp_file_path(browser, "diff")

    for url, scr in [
        (browser.prod_url, prod_screenshot_path),
        (browser.stag_url, stag_screenshot_path),
    ]:
        browser.get(url)
        browser.find_element(value="form-currency").click()
        browser.save_screenshot(scr)

    comparison_test_light(
        prod_screenshot_path, stag_screenshot_path, diff_screenshot_path
    )
