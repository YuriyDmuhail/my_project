import pytest
from hw28.page_object.base_page import BasePage
from hw28.page_object.login_page import LoginPage
from hw28.page_object.signup_page import SignUpPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw28.locators.registration_success import RegistrationSuccess

@pytest.mark.usefixtures()
class TestRegistration:

    def test_registration(self, web_driver, fake_first_name, fake_last_name, fake_email, fake_password, ):
        frame = BasePage(driver=web_driver)

        frame.sign_in_button.click()

        frame = LoginPage(driver=web_driver)
        frame.registration_url.click()

        frame = SignUpPage(driver=web_driver)

        frame.name_field.send_keys(fake_first_name)

        frame.last_name_field.send_keys(fake_last_name)

        frame.email_field.send_keys(fake_email)

        frame.password_field.send_keys("Fake_password1")

        frame.re_password_field.send_keys("Fake_password1")

        frame.register_btn.click()

        assert WebDriverWait(web_driver, 10).until(
            EC.presence_of_element_located(RegistrationSuccess.SUCCESS.value))

