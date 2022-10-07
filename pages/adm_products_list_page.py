import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdmProductsListPage(BasePage):

    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_MENU = (By.CSS_SELECTOR, "#menu-catalog li:nth-child(2) a")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "i.fa.fa-plus")
    PRODUCT_NAME = (By.NAME, "product_description[1][name]")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.note-editing-area p")
    PRODUCT_META_TAG_TITLE = (By.NAME, "product_description[1][meta_title]")
    PRODUCT_DATA_TAB = (By.XPATH, "//a[text()='Data']")
    PRODUCT_MODEL = (By.NAME, "model")
    PRODUCT_PRICE = (By.NAME, "price")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PRODUCT_NAMES_LIST = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(3)")
    PRODUCT_MODELS_LIST = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(2)")
    PRODUCTS_CHECKBOXES = (By.CSS_SELECTOR, "table.table tbody tr td:nth-child(1) input")
    NUM_OF_PRODUCTS = (By.CSS_SELECTOR, "div.col-sm-6.text-right")
    DELETE_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")

    TIMEOUT_FOR_ELEMENTS = 3

    @allure.step("Открываю список продуктов в админке")
    def open_adm_products_list_page(self):
        self.click(self.CATALOG_MENU, self.TIMEOUT_FOR_ELEMENTS)
        self.click(self.PRODUCTS_MENU, self.TIMEOUT_FOR_ELEMENTS)

    def open_product_data_tab(self):
        self.click(self.PRODUCT_DATA_TAB, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Создаю новый продукт со значениями: {product}")
    def create_new_product(self, product):
        self.click(self.ADD_PRODUCT_BUTTON, self.TIMEOUT_FOR_ELEMENTS)
        self.enter_text_in_field(self.PRODUCT_NAME, self.TIMEOUT_FOR_ELEMENTS, product.product_name)
        self.enter_text_in_field(self.PRODUCT_DESCRIPTION, self.TIMEOUT_FOR_ELEMENTS, product.description)
        self.enter_text_in_field(self.PRODUCT_META_TAG_TITLE, self.TIMEOUT_FOR_ELEMENTS, product.meta_tag_title)
        self.open_product_data_tab()
        self.enter_text_in_field(self.PRODUCT_MODEL, self.TIMEOUT_FOR_ELEMENTS, product.model)
        self.enter_text_in_field(self.PRODUCT_PRICE, self.TIMEOUT_FOR_ELEMENTS, product.price)
        self.click(self.SAVE_PRODUCT_BUTTON, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Проверяю, есть ли созданный продукт в списке")
    def is_new_product(self, product):
        names = self.find_elements(self.PRODUCT_NAMES_LIST, self.TIMEOUT_FOR_ELEMENTS)
        count_names = 0
        for name in names:
            if self.get_text_element(name) == product.product_name:
                count_names += 1

        if count_names == 1:
            return True
        else:
            return False

    @allure.step("Получаю общее число продуктов в списке")
    def get_num_of_products(self):
        temp = self.get_text(self.NUM_OF_PRODUCTS, self.TIMEOUT_FOR_ELEMENTS)
        num = int(temp.split()[5])
        return num

    @allure.step("Удаляю первый продукт в списке")
    def delete_first_product(self):
        checkboxes = self.find_elements(self.PRODUCTS_CHECKBOXES, self.TIMEOUT_FOR_ELEMENTS)
        self.click_element(checkboxes[0])
        self.click(self.DELETE_PRODUCTS_BUTTON, self.TIMEOUT_FOR_ELEMENTS)
        self.accept_alert(self.TIMEOUT_FOR_ELEMENTS)
