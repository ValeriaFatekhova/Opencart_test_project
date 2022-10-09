from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    PRODUCT_REVIEW = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(2)")
    THUMBNAILS = (By.CSS_SELECTOR, ".thumbnails")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    RATING = (By.CSS_SELECTOR, ".rating")

    TIMEOUT_FOR_ELEMENTS = 3

    def open_product_page(self, url):
        self.open_page(url)

    def is_thumbnails(self):
        self.find_element(self.THUMBNAILS, self.TIMEOUT_FOR_ELEMENTS)

    def is_product_description(self):
        self.find_element(self.PRODUCT_DESCRIPTION, self.TIMEOUT_FOR_ELEMENTS)

    def is_product_review(self):
        self.find_element(self.PRODUCT_REVIEW, self.TIMEOUT_FOR_ELEMENTS)

    def is_add_to_cart_button(self):
        self.find_element(self.ADD_TO_CART_BUTTON, self.TIMEOUT_FOR_ELEMENTS)

    def is_rating(self):
        self.find_element(self.RATING, self.TIMEOUT_FOR_ELEMENTS)
