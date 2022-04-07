from pages.main_page import MainPage
from pages.out_page import OutPage

def open_main_page(browser):
    link = "https://teamcapybara.github.io/capybara/"
    page = MainPage(browser, link)
    page.open()
    return page


def test_guest_should_see_mailing_list_btn(browser):
    page = open_main_page(browser)
    page.should_be_mailing_list_btn()


def test_guest_should_see_api_documentation_btn(browser):
    page = open_main_page(browser)
    page.should_be_api_documentation_btn()


def test_guest_should_see_source_code_btn(browser):
    page = open_main_page(browser)
    page.should_be_source_code_btn()


def test_guest_should_see_ruby_btn(browser):
    page = open_main_page(browser)
    page.should_be_ruby_btn()


def test_guest_should_see_readme_btn(browser):
    page = open_main_page(browser)
    page.should_be_readme_btn()


def test_guest_should_see_elabs_btn(browser):
    page = open_main_page(browser)
    page.should_be_elabs_btn()


def test_guest_should_see_elabs_symbol(browser):
    page = open_main_page(browser)
    page.should_be_elabs_symbol()


def test_guest_can_go_to_mailing_list_page(browser):
    page = open_main_page(browser)
    page.go_to_mailing_list()
    mailing_list_page = OutPage(browser, browser.current_url)
    browser.switch_to.window(browser.window_handles[1])
    mailing_list_page.should_be_url('https://groups.google.com/g/ruby-capybara')


def test_guest_can_go_to_api_documentation_page(browser):
    page = open_main_page(browser)
    page.go_to_api_documentation()
    api_documentation_page = OutPage(browser, browser.current_url)
    browser.switch_to.window(browser.window_handles[1])
    api_documentation_page.should_be_url('https://rubydoc.info/github/teamcapybara/capybara/master')


def test_guest_can_go_to_source_code_page(browser):
    page = open_main_page(browser)
    page.go_to_source_code()
    source_code_page = OutPage(browser, browser.current_url)
    browser.switch_to.window(browser.window_handles[1])
    source_code_page.should_be_url('https://github.com/teamcapybara/capybara')


def test_guest_can_go_to_ruby_page(browser):
    page = open_main_page(browser)
    page.go_to_ruby()
    ruby_page = OutPage(browser, browser.current_url)
    ruby_page.should_be_url('http://www.ruby-lang.org/ru/')


def test_guest_can_readme_page(browser):
    page = open_main_page(browser)
    page.go_to_readme()
    readme_page = MainPage(browser, browser.current_url)
    readme_page.should_be_url('https://rubydoc.info/github/teamcapybara/capybara')


def test_guest_can_elabs_page(browser):
    page = open_main_page(browser)
    page.go_to_elabs()
    elabs_page = MainPage(browser, browser.current_url)
    elabs_page.should_be_url('http://www.elabs.se/')


def test_guest_can_elabs_symbol_page(browser):
    page = open_main_page(browser)
    page.go_to_elabs_symbol()
    elabs_page = MainPage(browser, browser.current_url)
    elabs_page.should_be_url('http://www.elabs.se/')
#Тут есть спорный момент http://www.elabs.se/ - нерабочая ссылка
#http://www.elabs.se/ - рабочая
#Т.к у меня нет документации я не знаю верный ожидаемый результат
#Поэтому проверил, что открывается именно http://www.elabs.se/


def test_guest_can_see_copyright(browser):
    page = open_main_page(browser)
    page.copyright_should_be_true()