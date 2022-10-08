import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")
    REGISTRATION_ITEM = (By.CSS_SELECTOR, "ul.dropdown-menu-right li:first-child a")
    FIRST_NAME_FIELD = (By.NAME, "firstname")
    LAST_NAME_FIELD = (By.NAME, "lastname")
    EMAIL_FIELD = (By.NAME, "email")
    PHONE_FIELD = (By.NAME, "telephone")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value = 'Continue']")
    CONTENT_TITLE = (By.CSS_SELECTOR, "#content h1")

    TIMEOUT_FOR_ELEMENTS = 3

    @allure.step("Открываю страницу регистрации пользователя")
    def open_registration_page(self, url):
        self.open_page(url)
        self.click(self.MY_ACCOUNT, self.TIMEOUT_FOR_ELEMENTS)
        self.click(self.REGISTRATION_ITEM, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Создаю пользователя со значениями {user}")
    def create_random_user(self, user):
        self.logger.debug("__________Creating new user is started__________")
        self.logger.debug(f"User parameters: {user}")
        self.enter_text_in_field(self.FIRST_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.first_name)
        self.enter_text_in_field(self.LAST_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.last_name)
        self.enter_text_in_field(self.EMAIL_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.e_mail)
        self.enter_text_in_field(self.PHONE_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.phone)
        self.enter_text_in_field(self.PASSWORD_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.password)
        self.enter_text_in_field(self.CONFIRM_PASSWORD_FIELD, self.TIMEOUT_FOR_ELEMENTS, user.password)
        self.click(self.PRIVACY_POLICY_CHECKBOX, self.TIMEOUT_FOR_ELEMENTS)
        self.click(self.CONTINUE_BUTTON, self.TIMEOUT_FOR_ELEMENTS)
        self.logger.debug("__________Creating new user is finished__________")

    def get_content_title(self):
        return self.get_text(self.CONTENT_TITLE, self.TIMEOUT_FOR_ELEMENTS)
