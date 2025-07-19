import faker
import pytest
from selenium import webdriver
from hw28.page_object.base_page import BasePage
from faker import Faker
import random




@pytest.fixture(scope="session")
def web_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BasePage.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def fake_first_name():
    result = Faker()
    yield result.first_name()

@pytest.fixture(scope="session")
def fake_last_name():
    result = Faker()
    yield result.last_name()

@pytest.fixture(scope="session")
def fake_email():
    result = Faker()
    yield result.email()

@pytest.fixture(scope="session")
def fake_password():
    result = Faker()
    yield result.password(length=8)
