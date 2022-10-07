import allure
from pages.user_login_page import UserLoginPage


"""User login page tests"""


@allure.title("Проверка наличия поля 'Имя пользователя' на странице логина")
def test_ul_firstname_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_first_name_field()


@allure.title("Проверка наличия поля 'Фамилия пользователя' на странице логина")
def test_ul_lastname_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_last_name_field()


@allure.title("Проверка наличия поля 'Email' на странице логина")
def test_ul_email_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_email_field()


@allure.title("Проверка наличия правого меню на странице логина")
def test_ul_right_menu(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_right_menu()
    user_page.check_menu_items()


@allure.title("Проверка наличия кнопки 'Продолжить' на странице логина")
def test_ul_continue_button(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_continue_button()
