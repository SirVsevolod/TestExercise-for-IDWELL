from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
TIMEOUT = 4

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def btn_text_is_text(self, how, what, text):
        btn_text = self.browser.find_element(how, what).text
        assert btn_text == text, "btn text isn't" + text

    def go_to(self, how, what,):
        btn = self.browser.find_element(how, what)
        btn.click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def should_be_url(self, url):
        assert self.browser.current_url == url, "uncorrect url"

    def wait_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"element with locator {locator} not found")
        return element
