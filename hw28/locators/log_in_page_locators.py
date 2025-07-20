from enum import Enum
from selenium.webdriver.common.by import By

class LogInPageLocators(Enum):
    REGISTRATION_URL = (By.XPATH, "//button[text()='Registration']")