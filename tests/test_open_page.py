import pytest
from pages.home_page import HomePage
from utils.locators import Home

@pytest.mark.usefixtures("driver", "url")
def test_home_page(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)

    print("Opened the home page")

    # Call the accept_cookies method without passing any argument
    accept_button = home_page.accept_cookies()

    print("Clicked on the Accept button")

    # Click the Accept button
    accept_button.click()
    print("Accept button clicked")

    # Confirm the presence of Greyp logo
    home_page.confirm_greyp_logo()

    print("Greyp logo confirmation complete")

