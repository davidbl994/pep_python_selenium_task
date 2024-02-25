from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.locators import ESuv

class ESuvPage:

    def __init__(self, driver):
        self.driver = driver

    def open_esuv_page(self, esuv_url):
        self.driver.get(esuv_url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_header_visible(self):
        header = self.driver.find_element(*ESuv.HEADER_ESUV)
        return header.is_displayed()

    def is_bike_model_listed(self, model):
        bike_models = self.driver.find_elements(*ESuv.BIKE_MODEL)
        return any(model in bike_model.get_attribute('href') for bike_model in bike_models)

    def accept_cookies(self):
        # Wait for the Accept button to be clickable
        accept_button = self.wait_for_element(ESuv.ACCEPT)
        # Find and return the Accept button element
        return accept_button

    def select_bikes_for_comparison(self):
        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Select "T5.0" bike
        t50_bike_checkbox = self.driver.find_element(*ESuv.COMPARE_T50_BOX)
        actions.move_to_element(t50_bike_checkbox).click().perform()

        # Select "T5.1" bike
        t51_bike_checkbox = self.driver.find_element(*ESuv.COMPARE_T51_BOX)
        actions.move_to_element(t51_bike_checkbox).click().perform()

        # Wait for the URL to contain the parameters ?bike1=77&bike2=39
        WebDriverWait(self.driver, 10).until(EC.url_contains("?bike1=77&bike2=39"))

        return self.driver.current_url  # Return the current URL

    def is_compared_products_visible(self, expected_url):
        # Check the current URL and navigate back to the expected URL if it has changed
        if self.driver.current_url != expected_url:
            self.driver.get(expected_url)

            # Reselect the checkboxes
            t50_bike_checkbox = self.driver.find_element(*ESuv.COMPARE_T50_BOX)
            t51_bike_checkbox = self.driver.find_element(*ESuv.COMPARE_T51_BOX)
            self.driver.execute_script("arguments[0].click();", t50_bike_checkbox)
            self.driver.execute_script("arguments[0].click();", t51_bike_checkbox)

        compared_products = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(ESuv.COMPARED_PRODUCTS))
        compared_products.click()
        return compared_products

    def compare_now_select(self):
        compare_now = self.wait_for_element(ESuv.COMPARE_NOW)
        compare_now.click()
