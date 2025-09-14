import pytest
from selenium import webdriver
from hw27.classes import BaseNovaPost

@pytest.fixture(scope="session")
def web_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BaseNovaPost.BASE_URL)
    yield driver
    driver.quit()