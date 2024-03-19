import pytest
from ...pages.esuv_page import ESuvPage

@pytest.mark.usefixtures("driver", "esuv_url")
def test_bike_models_listing(driver, esuv_url):
    esuv_page = ESuvPage(driver)
    print("Opening eSUV page...")
    esuv_page.open_esuv_page(esuv_url)

    # Accept cookies
    print("Accepting cookies...")
    accept_button = esuv_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Check that the header is visible
    print("Checking the header...")
    assert esuv_page.is_header_visible(), "Header is not visible"

    # Define the expected bike models
    expected_bike_models = ['t50', 't51', 't52']

    # Check that the expected bike models are listed
    print("Checking the bike models...")
    for model in expected_bike_models:
        assert esuv_page.is_bike_model_listed(model), f"Bike model {model} is not listed"
