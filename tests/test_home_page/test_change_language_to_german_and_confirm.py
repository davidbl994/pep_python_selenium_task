import pytest
from ...pages.home_page import HomePage

@pytest.mark.usefixtures("driver", "home_url")
def test_change_language_to_german(driver, home_url):
    home_page = HomePage(driver)
    home_page.open_home_page(home_url)

    # Accept cookies
    accept_button = home_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Click the German language button
    assert home_page.click_german(), "Failed to click the German language button"

    # Confirm the language change
    header_text = home_page.get_header_text()
    assert header_text, "Failed to get the header text"

    assert home_page.driver.current_url == 'https://www.greyp.com/de/', "Failed to navigate to the German home page"
    assert "LIEBE GREYP-GEMEINDE," in header_text, "Failed to change language to German"