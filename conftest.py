import ssl
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

ssl._create_default_https_context = ssl._create_unverified_context

# CONSTANTS

HOME_PAGE = 'https://www.greyp.com/en/'
EPOWER_PAGE = 'https://www.greyp.com/en/epower/'
ESUV_PAGE = 'https://www.greyp.com/en/esuv/'
COMPARISON_PAGE = 'https://www.greyp.com/en/comparator/'

@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()

    # Set up chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Create the Webdriver with the specified
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def home_url():
    return HOME_PAGE

@pytest.fixture
def epower_url():
    return EPOWER_PAGE

@pytest.fixture
def esuv_url():
    return ESUV_PAGE

@pytest.fixture
def comparison_url():
    return COMPARISON_PAGE
