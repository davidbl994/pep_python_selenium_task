from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ..utils.locators import EPower

class EPowerPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_epower_page(self, epower_url):
        self.driver.get(epower_url)

    def is_correct_header_text(self):
        header = self.wait_for_element(EPower.HEADER_H1)
        return header.text == "HACK THE HILLS"

    def accept_cookies(self):
        # Wait for the Accept button to be clickable
        accept_button = self.wait_for_element(EPower.ACCEPT)
        # Find and return the Accept button element
        return accept_button

    def is_bike_list_visible(self):
        bike_list = self.wait_for_element(EPower.BIKE_LIST)
        bike_anchors = bike_list.find_elements(By.TAG_NAME, "a")
        return len(bike_anchors) == 9

    def click_learn_more(self):
        try:
            learn_more_button = self.driver.find_element(*EPower.LEARN_MORE_BUTTON)
            learn_more_button.click()
            return True
        except Exception as e:
            print(f"Failed to click the Learn More button: {e}")
            return False

    def hover_and_see_more(self):
        bike_image = self.driver.find_element(*EPower.BIKE_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(bike_image).perform()
        see_more = self.wait_for_element(EPower.SEE_MORE)
        return see_more.is_displayed()

    def click_compare(self):
        try:
            compare_checkbox = self.driver.find_element(*EPower.COMPARE)
            compare_checkbox.click()
            return True
        except Exception as e:
            print(f"Failed to click the Compare checkbox: {e}")
            return False

    def is_compared_products_visible(self):
        compared_products = self.wait_for_element(EPower.COMPARED_PRODUCTS)
        return compared_products.is_displayed()
