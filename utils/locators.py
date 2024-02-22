from selenium.webdriver.common.by import By

class Home:
    ACCEPT = (By.XPATH, '//button[text()="Accept all cookies"]')
    GREYP_LOGO = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/a/img')
    GERMAN = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[2]/ul/li[3]/a[2]')
    ENGLISH = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[2]/ul/li[3]/a[1]')
    ePOWER = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/ul/li[1]/a')
    eSUV = (By.XPATH, '//*[@id="__layout"]/main/div/nav/div/div[1]/ul/li[2]/a')
    DASHBOARD = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/section[2]/div[2]/div/div[1]/div/a')
    MESSAGE_GER = (By.XPATH, '//*[@id="__layout"]/main/div/div[1]/header/h1/span')
