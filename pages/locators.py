from selenium.webdriver.common.by import By


class MainPageLocators():
    MAILING_LIST_BTN = (By.CSS_SELECTOR, ".links > li:nth-child(1) > a")
    API_DOCUMENTATION_BTN = (By.CSS_SELECTOR, ".links > li:nth-child(2) > a")
    SOURCE_CODE_BTN = (By.CSS_SELECTOR, ".links > li:nth-child(3) > a")
    RUBY_BTN = (By.CSS_SELECTOR, '.intro > p > a')
    README_BTN = (By.CSS_SELECTOR, '.code > p > a')
    ELABS_BTN = (By.CSS_SELECTOR, '.footer > p > a')
    ELABS_SYMBOL = (By.CSS_SELECTOR, '.elabs-symbol')
    COPYRIGHT_TEXT = (By.CSS_SELECTOR, '.footer > p')