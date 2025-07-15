from enum import Enum
from selenium.webdriver.common.by import By

class DzFrameFirstLocator(Enum):
    INPUT_FIELD = (By.ID, "input1")
    VERIFY_INPUT_BUTTON = (By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")

class DzFrameSecondLocator(Enum):
    INPUT_FIELD = (By.ID, "input2")
    VERIFY_INPUT_BUTTON = (By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")  # fixed: input12 → input2
