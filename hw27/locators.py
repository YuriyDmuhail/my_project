from enum import Enum
from selenium.webdriver.common.by import By

class LocatorsNovaPost(Enum):
    INPUT_FIELD = (By.ID, "en")
    SEARCH_BUTTON = (By.ID, "np-number-input-desktop-btn-search-en")
    ACCEPT_INSTRUCTIONS = (By.CSS_SELECTOR, "span.v-btn__content")
    CHECK_STATUS = (By.CSS_SELECTOR, "div.header__status-text")

