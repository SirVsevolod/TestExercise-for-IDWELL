import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart chrome browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

capabilities = {
    "browserName": "chrome",
    "--nosandbox": True,
    "browserVersion": "99.0",
    "screenResolution": "1920x1080x24",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False,
    }
}
#
#

@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities
    )
    yield browser
    print("\nquit browser..")
    browser.quit()



