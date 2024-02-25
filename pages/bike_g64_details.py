from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.locators import G64

class BikeDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_correct_bike_name(self):
        bike_name = self.wait_for_element(G64.BIKE_NAME)
        return bike_name.text == 'G6.4'

    def select_size(self, size):
        try:
            # Wait for the size button to be clickable
            wait = WebDriverWait(self.driver, 10)
            size_button = wait.until(EC.element_to_be_clickable(G64.M_SIZE))

            size_button.click()
            return True
        except Exception as e:
            print(f"Failed to select size {size}: {e}")
            return False

    def is_correct_size_selected(self, size):
        size_button = self.driver.find_element(*getattr(G64, f"{size}_SIZE"))
        parent_li = size_button.find_element(By.XPATH, '..')
        return 'isActive' in parent_li.get_attribute('class')

    def is_rider_height_visible(self):
        rider_height = self.wait_for_element(G64.RIDER_HEIGHT)
        return rider_height.is_displayed()

    def select_engine(self, engine):
        try:
            # Wait for the engine button to be clickable
            wait = WebDriverWait(self.driver, 10)
            engine_button = wait.until(EC.element_to_be_clickable(G64.ENGINE))

            engine_button.click()
            return True
        except Exception as e:
            print(f"Failed to select engine {engine}: {e}")
            return False

    def is_correct_engine_selected(self, engine):
        if engine == '460W | 45 km/h':
            engine_button = self.driver.find_element(*G64.ENGINE)
            parent_li = engine_button.find_element(By.XPATH, '..')
            return 'isActive' in parent_li.get_attribute('class')