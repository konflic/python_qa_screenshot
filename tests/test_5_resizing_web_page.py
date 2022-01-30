import allure
import pytest

from screenshots.helpers import comparison_test_light, make_tmp_file


@pytest.mark.parametrize("screen", ["640x700", "1024x768", "1920x1080"])
@allure.title("Comparing pages with rectangles: {screen}")
def test_main_page_scaling(browser, screen):
    browser.set_window_size(*screen.split("x"))
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")
    diff_path = make_tmp_file(browser, "diff")

    browser.get(browser.prod_url)
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    comparison_test_light(
        master_path,
        staging_path,
        diff_path,
        clear_images=False
    )
