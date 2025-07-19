from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw28.page_object.base_page import BasePage
from hw28.locators.sign_up_page_locators import SignUpPageLocators

class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def name_field(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_NAME.value))

    @property
    def last_name_field(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_LAST_NAME.value))

    @property
    def email_field(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_EMAIL.value))

    @property
    def password_field(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_PASSWORD.value))

    @property
    def re_password_field(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_RE_PASSWORD.value))

    @property
    def register_btn(self):
        return self.wait.until(EC.element_to_be_clickable(SignUpPageLocators.S_UP_REGISTER_BTN.value))