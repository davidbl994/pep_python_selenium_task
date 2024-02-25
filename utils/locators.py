from selenium.webdriver.common.by import By

class BasePage:
    ACCEPT = (By.XPATH, '//button[text()="Accept all cookies"]')
class Home(BasePage):
    GREYP_LOGO = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/a/img')
    GERMAN = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[2]/ul/li[3]/a[2]')
    ENGLISH = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[2]/ul/li[3]/a[1]')
    EPOWER = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/ul/li[1]/a')
    ESUV = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/ul/li[2]/a')
    DASHBOARD = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/section[2]/div[2]/div/div[1]/div/a')
    MESSAGE_GER = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/section[1]/div/h3')

class EPower(BasePage):
    HEADER_H1 = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/header/div/h1/div')
    BIKE_LIST = (By.CLASS_NAME, "products")
    LEARN_MORE_BUTTON = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/div[1]/section/a[1]/div[2]/button')
    BIKE_IMAGE = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/div[1]/section/a[4]/div[1]/img')
    SEE_MORE = (By.LINK_TEXT, "See more")
    COMPARE = (By.XPATH, '//*[@id="__layout"]/main/div[1]/section/div/div[1]/section/a[1]/div[2]/label/span')
    COMPARED_PRODUCTS = (By.XPATH, '//*[@id="__layout"]/main/div[2]/button/span')

class G64:
    BIKE_NAME = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/div/header/aside/h1')
    M_SIZE = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/div/header/aside/ul[1]/li[2]/button')
    RIDER_HEIGHT = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/div/header/aside/h6')
    ENGINE = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/div/header/aside/ul[2]/li[2]/button')

class ESuv(BasePage):
    HEADER_ESUV = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/header/div/h1/div')
    BIKE_MODEL = (By.CSS_SELECTOR, ".products__Item")
    COMPARE_T50_BOX = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/div[1]/section/a[1]/div[2]/label/span')
    COMPARE_T51_BOX = (By.XPATH, '//*[@id="__layout"]/main/div/section/div/div[1]/section/a[2]/div[2]/label/span')
    COMPARED_PRODUCTS = (By.XPATH, '//*[@id="__layout"]/main/div[2]/button/span')
    COMPARE_NOW = (By.XPATH, '//*[@id="__layout"]/main/div[3]/div/div[3]/a')

class Comparison:
    T50_NAME = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/div[1]/h3')
    T51_NAME = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/div[2]/h3')
    T50_IMAGE = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/div[1]/div[2]/img')
    T51_IMAGE = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/div[2]/div[2]/img')
    CLOSE_COMPARATOR = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[5]/button')