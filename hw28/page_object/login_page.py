from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw28.page_object.base_page import BasePage
from hw28.locators.log_in_page_locators import LogInPageLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def registration_url(self):
        return self.wait.until(EC.element_to_be_clickable(LogInPageLocators.REGISTRATION_URL.value))
