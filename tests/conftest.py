import pytest
from selenium import webdriver

from pages.admin_login_page import AdminLoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser for tests")
    parser.addoption("--driver", default="C:\\drivers\\", help="Path to folder with drivers")
    parser.addoption("--url", default="http://localhost/", help="Url for test opencart")


@pytest.fixture(scope="function")
def driver(request):
    _browser = request.config.getoption("--browser")
    _driver_path = request.config.getoption("--driver")

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{_driver_path}chromedriver.exe")
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{_driver_path}geckodriver.exe")
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{_driver_path}operadriver.exe")
    else:
        raise ValueError(f"Browser {_browser} not supported")

    yield driver
    driver.close()


@pytest.fixture(scope="function")
def url(request):
    yield request.config.getoption("--url")


@pytest.fixture()
def admin_login(driver, url):
    al = AdminLoginPage(driver)
    al.open_admin_login_page(url)
    al.login_to_admin("user", "bitnami")
