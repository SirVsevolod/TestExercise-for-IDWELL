from pages.locators import MainPageLocators
from pages.base_page import BasePage



class MainPage(BasePage):
    def should_be_mailing_list_btn(self):
        self.btn_text_is_text(*MainPageLocators.MAILING_LIST_BTN, 'Mailing list')

    def should_be_api_documentation_btn(self):
        self.btn_text_is_text(*MainPageLocators.API_DOCUMENTATION_BTN, 'API documentation')

    def should_be_source_code_btn(self):
        self.btn_text_is_text(*MainPageLocators.SOURCE_CODE_BTN, 'Source code')

    def should_be_ruby_btn(self):
        self.btn_text_is_text(*MainPageLocators.RUBY_BTN, 'Ruby')

    def should_be_readme_btn(self):
        self.btn_text_is_text(*MainPageLocators.README_BTN, 'README')

    def should_be_elabs_btn(self):
        self.btn_text_is_text(*MainPageLocators.ELABS_BTN, 'Elabs')

    def should_be_elabs_symbol(self):
        self.is_element_present(*MainPageLocators.ELABS_SYMBOL)

    def go_to_mailing_list(self):
        btn = self.wait_clickable(MainPageLocators.MAILING_LIST_BTN)
        btn.click()

    def go_to_api_documentation(self):
        btn = self.wait_clickable(MainPageLocators.API_DOCUMENTATION_BTN)
        btn.click()

    def go_to_source_code(self):
        btn = self.wait_clickable(MainPageLocators.SOURCE_CODE_BTN)
        btn.click()

    def go_to_ruby(self):
        btn = self.wait_clickable(MainPageLocators.RUBY_BTN)
        btn.click()

    def go_to_readme(self):
        btn = self.wait_clickable(MainPageLocators.README_BTN)
        btn.click()

    def go_to_elabs(self):
        btn = self.wait_clickable(MainPageLocators.ELABS_BTN)
        btn.click()

    def go_to_elabs_symbol(self):
        btn = self.wait_clickable(MainPageLocators.ELABS_BTN)
        btn.click()

    def copyright_should_be_true(self):
        copyright_text = self.browser.find_element(*MainPageLocators.COPYRIGHT_TEXT).text
        assert copyright_text == '© 2011 - Site lovingly crafted by Elabs\nElabs', "copyright is false"