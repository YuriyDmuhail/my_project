from enum import Enum
from selenium.webdriver.common.by import By

class RegistrationSuccess(Enum):
    SUCCESS = (By.XPATH, "//p[text()='Registration complete']")