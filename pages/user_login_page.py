import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserLoginPage(BasePage):

    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD= (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    PHONE_FIELD = (By.ID, "input-telephone")
    RIGHT_MENU = (By.ID, "column-right")
    MENU_ITEMS = (By.CSS_SELECTOR, "#column-right div a")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#column-right div a")

    TIMEOUT_FOR_ELEMENTS = 3
    USER_LOGIN_URL = "index.php?route=account/register"

    MENU_LIST = [
        ("Login", "http://localhost/index.php?route=account/login"),
        ("Register", "http://localhost/index.php?route=account/register"),
        ("Forgotten Password", "http://localhost/index.php?route=account/forgotten"),
        ("My Account", "http://localhost/index.php?route=account/account"),
        ("Address Book", "http://localhost/index.php?route=account/address"),
        ("Wish List", "http://localhost/index.php?route=account/wishlist"),
        ("Order History", "http://localhost/index.php?route=account/order"),
        ("Downloads", "http://localhost/index.php?route=account/download"),
        ("Recurring payments", "http://localhost/index.php?route=account/recurring"),
        ("Reward Points", "http://localhost/index.php?route=account/reward"),
        ("Returns", "http://localhost/index.php?route=account/return"),
        ("Transactions", "http://localhost/index.php?route=account/transaction"),
        ("Newsletter", "http://localhost/index.php?route=account/newsletter"),
    ]

    def open_user_login_page(self, url):
        self.open_page(url+self.USER_LOGIN_URL)

    def is_first_name_field(self):
        self.find_element(self.FIRST_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS)

    def is_last_name_field(self):
        self.find_element(self.LAST_NAME_FIELD, self.TIMEOUT_FOR_ELEMENTS)

    def is_email_field(self):
        self.find_element(self.EMAIL_FIELD, self.TIMEOUT_FOR_ELEMENTS)

    def is_continue_button(self):
        self.find_element(self.CONTINUE_BUTTON, self.TIMEOUT_FOR_ELEMENTS)

    def is_right_menu(self):
        self.find_element(self.RIGHT_MENU, self.TIMEOUT_FOR_ELEMENTS)

    @allure.step("Првоеряю правое меню на странице логина пользователя")
    def check_menu_items(self):
        elements = self.find_elements(self.MENU_ITEMS, self.TIMEOUT_FOR_ELEMENTS)
        for i in range(len(elements)):
            temp = (elements[i].text, elements[i].get_attribute("href"))
            if temp != self.MENU_LIST[i]:
                raise AssertionError("Menu items are incorrect")

