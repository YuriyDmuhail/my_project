from enum import Enum
from selenium.webdriver.common.by import By

class BasePageLocators(Enum):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-white.header_signin")