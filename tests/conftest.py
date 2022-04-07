import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()