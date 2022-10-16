import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):

    USER_NAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "span.help-block")
    ADMIN_LOGO = (By.ID, "header-logo")
    ADMIN_LOGO_LINK = (By.CSS_SELECTOR, "#header-logo a")

    TIMEOUT_FOR_ELEMENTS = 3
    ADMIN_URL = "admin"
    ADMIN_LINK = "http://localhost/admin/index.php?route=common/login"

    def open_admin_login_page(self, url):
        self.open_page(url+self.ADMIN_URL)

    def is_user_name_field(self):
        self.find_element(self.USER_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS)

    def is_password_field(self):
        self.find_element(self.PASSWORD_FIELD, self.TIMEOUT_FOR_ELEMENTS)

    def is_login_button(self):
        self.find_element(self.LOGIN_BUTTON, self.TIMEOUT_FOR_ELEMENTS)

    def is_forgotten_password_link(self):
        self.find_element(self.FORGOTTEN_PASSWORD, self.TIMEOUT_FOR_ELEMENTS)

    def is_admin_logo(self):
        self.find_element(self.ADMIN_LOGO, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Проверяю ссылку логотипа в админке")
    def check_logo_link(self):
        if self.get_element_link(self.ADMIN_LOGO_LINK, self.TIMEOUT_FOR_ELEMENTS) != self.ADMIN_LINK:
            raise AssertionError("Admin Logo link is incorrect")

    @allure.step("Логин в админку с параметрами: user {user}, password {password}")
    def login_to_admin(self, user, password):
        self.find_element(self.USER_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS).send_keys(user)
        self.find_element(self.PASSWORD_FIELD, self.TIMEOUT_FOR_ELEMENTS).send_keys(password)
        self.find_element(self.LOGIN_BUTTON, self.TIMEOUT_FOR_ELEMENTS).click()
