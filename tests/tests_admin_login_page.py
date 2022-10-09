from pages.admin_login_page import AdminLoginPage


"""Admin login page tests"""


def test_admin_login_page_logo(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_admin_logo()
    admin_page.check_logo_link()


def test_al_username_field(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_user_name_field()


def test_al_password_field(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_password_field()


def test_al_login_button(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_login_button()


def test_al_forgotten_password_link(driver, url):
    admin_page = AdminLoginPage(driver)
    admin_page.open_admin_login_page(url)
    admin_page.is_forgotten_password_link()
