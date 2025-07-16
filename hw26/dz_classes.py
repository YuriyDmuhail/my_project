from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw26.locators import DzFrameFirstLocator, DzFrameSecondLocator


class BaseDzFront:
    BASE_URL = "http://localhost:8000/dz.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

class FrameOne(BaseDzFront):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def input_field(self):
        return self.wait.until(EC.element_to_be_clickable(DzFrameFirstLocator.INPUT_FIELD.value))

    @property
    def verify_input_button(self):
        return self.wait.until(EC.element_to_be_clickable(DzFrameFirstLocator.VERIFY_INPUT_BUTTON.value))

class FrameTwo(BaseDzFront):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def input_field(self):
        return self.wait.until(EC.element_to_be_clickable(DzFrameSecondLocator.INPUT_FIELD.value))

    @property
    def verify_input_button(self):
        return self.wait.until(EC.element_to_be_clickable(DzFrameSecondLocator.VERIFY_INPUT_BUTTON.value))
