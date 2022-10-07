import allure
from pages.admin_login_page import AdminLoginPage


"""Admin login page tests"""


@allure.title("Проверка логотипа на странице логина в админку")
def test_admin_login_page_logo(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_admin_logo()
    admin_page.check_logo_link()


@allure.title("Проверка наличия поля 'Имя пользователя' на странице логина в админку")
def test_al_username_field(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_user_name_field()


@allure.title("Проверка наличия поля 'Пароль' на странице логина в админку")
def test_al_password_field(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_password_field()


@allure.title("Проверка наличия кнопки 'Логин' на странице логина в админку")
def test_al_login_button(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_login_button()


@allure.title("Проверка наличия ссылки для восстановления пароля на странице логина в админку")
def test_al_forgotten_password_link(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_forgotten_password_link()
