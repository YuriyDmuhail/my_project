import pytest
from selenium import webdriver
from hw26.dz_classes import BaseDzFront

@pytest.fixture(scope="session")
def web_driver_dz_front():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BaseDzFront.BASE_URL)
    yield driver
    driver.quit()
