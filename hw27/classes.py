from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw27.locators import LocatorsNovaPost


class BaseNovaPost:
    BASE_URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    @property
    def input_field(self):
        return self.wait.until(EC.element_to_be_clickable(LocatorsNovaPost.INPUT_FIELD.value))

    @property
    def search_button(self):
        return self.wait.until(EC.element_to_be_clickable(LocatorsNovaPost.SEARCH_BUTTON.value))

    @property
    def through_instructions(self):
        return self.wait.until(EC.element_to_be_clickable(LocatorsNovaPost.ACCEPT_INSTRUCTIONS.value))

    @property
    def check_status(self):
        return self.wait.until(EC.element_to_be_clickable(LocatorsNovaPost.CHECK_STATUS.value))
