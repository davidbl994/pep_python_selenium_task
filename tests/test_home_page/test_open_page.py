import pytest
from ...pages.home_page import HomePage
@pytest.mark.usefixtures("driver", "home_url")
def test_home_page(driver, home_url):
    home_page = HomePage(driver)
    assert home_page.open_home_page(home_url), "Failed to open the home page"
    assert home_page.driver.current_url == home_url, "Failed to navigate to the home page"

    # Call the accept_cookies method without passing any argument
    accept_button = home_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"

    # Click the Accept button
    accept_button.click()

    # Confirm the presence of Greyp logo
    assert home_page.is_greyp_logo_displayed(), "Failed to confirm the Greyp logo"

