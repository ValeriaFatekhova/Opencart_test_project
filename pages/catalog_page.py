import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):

    LEFT_MENU = (By.ID, "column-left")
    CATALOG_CONTENT = (By.ID, "content")
    ACTIVE_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .active")
    EMPTY_CATALOG_MESSAGE = (By.CSS_SELECTOR, "#content>p")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout.product-grid")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    LIST_VIEW_BUTTON = (By.ID, "list-view")

    TIMEOUT_FOR_ELEMENTS = 3

    def open_catalog_page(self, url):
        self.open_page(url)

    def is_left_menu(self):
        self.find_element(self.LEFT_MENU, self.TIMEOUT_FOR_ELEMENTS)

    def is_catalog_content(self):
        self.find_element(self.CATALOG_CONTENT, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Получаю активный элемент меню")
    def get_active_menu_items(self):
        items = self.find_elements(self.ACTIVE_MENU_ITEMS, self.TIMEOUT_FOR_ELEMENTS)
        texts = []
        for i in items:
            texts.append(self.get_text_element(i))
        return texts

    def is_catalog_empty(self):
        self.find_element(self.EMPTY_CATALOG_MESSAGE, self.TIMEOUT_FOR_ELEMENTS)

    def get_products(self):
        return self.find_elements(self.PRODUCTS, self.TIMEOUT_FOR_ELEMENTS)

    def is_breadcrumbs(self):
        self.find_element(self.BREADCRUMB, self.TIMEOUT_FOR_ELEMENTS)

    def is_continue_button(self):
        self.find_element(self.CONTINUE_BUTTON, self.TIMEOUT_FOR_ELEMENTS)

    def is_list_view_button(self):
        self.find_element(self.LIST_VIEW_BUTTON, self.TIMEOUT_FOR_ELEMENTS)
