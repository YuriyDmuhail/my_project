from enum import Enum
from selenium.webdriver.common.by import By


# def name_field(self):
# def last_name_field(self):
# def email_field(self):
# def password_field(self):
# def re_enter_password_field(self):
# def register_btn(self): (By.ID, "") By.XPATH, "//button[text()='Registration']"

class SignUpPageLocators(Enum):
    S_UP_NAME = (By.ID, "signupName")
    S_UP_LAST_NAME = (By.ID, "signupLastName")
    S_UP_EMAIL = (By.ID, "signupEmail")
    S_UP_PASSWORD = (By.ID, "signupPassword")
    S_UP_RE_PASSWORD = (By.ID, "signupRepeatPassword")
    S_UP_REGISTER_BTN = (By.XPATH, "//button[text()='Register']")
    # S_UP_REGISTER_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary")