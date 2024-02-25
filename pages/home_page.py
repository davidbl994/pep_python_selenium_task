from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.locators import Home

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_home_page(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"Failed to open the home page: {e}")
            return False

    def accept_cookies(self):
        # Wait for the Accept button to be clickable
        accept_button = self.wait_for_element(Home.ACCEPT)
        # Find and return the Accept button element
        return accept_button

    def is_greyp_logo_displayed(self):
        greyp_logo_element = self.driver.find_element(*Home.GREYP_LOGO)
        return greyp_logo_element.is_displayed()

    def click_german(self):
        try:
            german_button = self.driver.find_element(*Home.GERMAN)
            german_button.click()
            return True
        except Exception as e:
            print(f"Failed to click the German language button: {e}")
            return False

    def get_header_text(self):
        header_element = self.driver.find_element(*Home.MESSAGE_GER)
        return header_element.text