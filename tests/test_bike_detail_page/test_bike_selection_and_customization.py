import pytest
from ...pages.epower_page import EPowerPage
from ...pages.bike_g64_details import BikeDetailPage

@pytest.mark.usefixtures("driver", "epower_url")
def test_bike_selection_and_customization(driver, epower_url):
    epower_page = EPowerPage(driver)
    epower_page.open_epower_page(epower_url)

    # Accept cookies
    accept_button = epower_page.accept_cookies()
    assert accept_button, "Failed to find the Accept button"
    accept_button.click()

    # Click on the "Learn more" button for a bike
    assert epower_page.click_learn_more(), "Failed to click the Learn more button"

    # Create a BikeDetailPage object
    bike_detail_page = BikeDetailPage(driver)

    # Check that the correct bike is opened
    assert bike_detail_page.is_correct_bike_name(), "Incorrect bike name"

    # Select size
    assert bike_detail_page.select_size('M'), "Failed to select size M"

    # Check that the correct size is selected
    assert bike_detail_page.is_correct_size_selected('M'), "Incorrect size selected"

    # Check that the rider height is visible
    assert bike_detail_page.is_rider_height_visible(), "Rider height is not visible"

    # Select engine
    assert bike_detail_page.select_engine('460W | 45 km/h'), "Failed to select engine 460W | 45 km/h"

    # Check that the correct engine is selected
    assert bike_detail_page.is_correct_engine_selected('460W | 45 km/h'), "Incorrect engine selected"