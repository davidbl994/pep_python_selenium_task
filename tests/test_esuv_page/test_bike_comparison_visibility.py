import pytest
from ...pages.esuv_page import ESuvPage
from ...pages.comparison_page import ComparisonPage

@pytest.mark.usefixtures("driver", "esuv_url")
def test_bike_comparison(driver, esuv_url):
    esuv_page = ESuvPage(driver)
    esuv_page.open_esuv_page(esuv_url)

    try:
        # Accept cookies
        esuv_page.accept_cookies().click()

        # Select both bikes for comparison and store the new URL
        comparison_url = esuv_page.select_bikes_for_comparison()

        # Click the "COMPARED PRODUCTS" button
        esuv_page.is_compared_products_visible(comparison_url)

        # Click the "Compare now" button
        esuv_page.compare_now_select()

        # Create a ComparisonPage object
        comparison_page = ComparisonPage(driver)

        # Check that the correct bikes are being compared
        assert comparison_page.is_correct_t50_bike_name(), "Incorrect T50 bike name"
        assert comparison_page.is_correct_t51_bike_name(), "Incorrect T51 bike name"

        # Check that the bike images are displayed
        assert comparison_page.is_t50_image_visible(), "T50 image is not visible"
        assert comparison_page.is_t51_image_visible(), "T51 image is not visible"

        # Check that the "Close Comparison" button is visible
        assert comparison_page.is_close_comparison_button_visible(), "Close Comparison button is not visible"

    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")