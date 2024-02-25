import pytest
from ...pages.epower_page import EPowerPage


@pytest.mark.usefixtures("driver", "epower_url")
def test_number_bikes_list(driver, epower_url):
    epower_page = EPowerPage(driver)
    epower_page.open_epower_page(epower_url)

    # Accept cookies
    accept_button = epower_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Check that the bike list is visible and contains nine bikes
    assert epower_page.is_bike_list_visible(), "Bike list is not visible or does not contain nine bikes"