from pages.user_login_page import UserLoginPage


"""User login page tests"""


def test_ul_firstname_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_first_name_field()


def test_ul_lastname_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_first_name_field()


def test_ul_email_field(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_email_field()


def test_ul_right_menu(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_right_menu()
    user_page.check_menu_items()


def test_ul_continue_button(driver, url):
    user_page = UserLoginPage(driver)
    user_page.open_user_login_page(url)
    user_page.is_continue_button()
