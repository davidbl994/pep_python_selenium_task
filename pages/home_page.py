from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Home

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self, url):
        self.driver.get(url)

    def accept_cookies(self):
        # Wait for the Accept button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept all cookies"]'))
        )
        # Find and return the Accept button element
        return self.driver.find_element(*Home.ACCEPT)

    def confirm_greyp_logo(self):
        greyp_logo_element = self.driver.find_element(*Home.GREYP_LOGO)
        assert greyp_logo_element.is_displayed()