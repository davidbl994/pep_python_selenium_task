import ssl
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ssl._create_default_https_context = ssl._create_unverified_context

@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()

    # Set up chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Create the Webdriver with the specified
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture
def url():
    return 'https://www.greyp.com/en/'