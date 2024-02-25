import pytest
from ...pages.epower_page import EPowerPage

@pytest.mark.usefixtures("driver", "epower_url")
def test_compared_products_appear_after_selecting_compare(driver, epower_url):
    epower_page = EPowerPage(driver)
    epower_page.open_epower_page(epower_url)

    # Accept cookies
    accept_button = epower_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Click on the "Compare" checkbox
    assert epower_page.click_compare(), "Failed to click the Compare checkbox"

    # Check that the "COMPARED PRODUCTS" button appears
    assert epower_page.is_compared_products_visible(), "Compared products button is not visible"
