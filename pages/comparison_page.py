from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.locators import Comparison

import logging

class ComparisonPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_comparison_page(self, comparison_url):
        self.driver.get(comparison_url)

    def is_correct_t50_bike_name(self):
        try:
            # Wait for the bike name element to be visible
            wait = WebDriverWait(self.driver, 10)
            bike_name_element = wait.until(EC.visibility_of_element_located(Comparison.T50_NAME))

            # Check that the bike name is correct
            return bike_name_element.text == 'T5.0'
        except Exception as e:
            print(f"Failed to check T50 bike name: {e}")
            return False

    def is_correct_t51_bike_name(self):
        try:
            # Wait for the bike name element to be visible
            wait = WebDriverWait(self.driver, 10)
            bike_name_element = wait.until(EC.visibility_of_element_located(Comparison.T51_NAME))

            # Check that the bike name is correct
            return bike_name_element.text == 'T5.1'
        except Exception as e:
            print(f"Failed to check T51 bike name: {e}")
            return False

    def is_t50_image_visible(self):
        try:
            t50_image = self.wait_for_element(Comparison.T50_IMAGE)
            return t50_image.is_displayed()
        except Exception as e:
            logging.error(e)
            return False

    def is_t51_image_visible(self):
        try:
            t51_image = self.wait_for_element(Comparison.T51_IMAGE)
            return t51_image.is_displayed()
        except Exception as e:
            logging.error(e)
            return False

    def is_close_comparison_button_visible(self):
        close_comparison_button = self.wait_for_element(Comparison.CLOSE_COMPARATOR)
        return close_comparison_button.is_displayed()