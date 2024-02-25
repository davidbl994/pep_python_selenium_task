import pytest
from ...pages.esuv_page import ESuvPage

@pytest.mark.usefixtures("driver", "esuv_url")
def test_bike_models_listing(driver, esuv_url):
    esuv_page = ESuvPage(driver)
    esuv_page.open_esuv_page(esuv_url)

    # Accept cookies
    accept_button = esuv_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Check that the header is visible
    assert esuv_page.is_header_visible(), "Header is not visible"

    # Define the expected bike models
    expected_bike_models = ['t50', 't51', 't52']

    # Check that the expected bike models are listed
    for model in expected_bike_models:
        assert esuv_page.is_bike_model_listed(model), f"Bike model {model} is not listed"
