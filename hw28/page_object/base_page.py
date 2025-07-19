from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw28.locators.base_page_locators import BasePageLocators

class BasePage:
    BASE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    @property
    def sign_in_button(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.SIGN_IN_BTN.value))

