import pytest
from selenium import webdriver

from pages.admin_login_page import AdminLoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser for tests")
    parser.addoption("--executor", action="store", default="192.168.1.114")
    parser.addoption("--driver", default="C:\\drivers\\", help="Path to folder with drivers")
    parser.addoption("--url", default="http://192.168.1.114:8081/", help="Url for test opencart")


@pytest.fixture(scope="function")
def driver(request):
    _browser = request.config.getoption("--browser")
    _driver_path = request.config.getoption("--driver")
    _executor = request.config.getoption("--executor")

    if _executor == "local":
        if _browser == "chrome":
            driver = webdriver.Chrome(executable_path=f"{_driver_path}chromedriver.exe")
        elif _browser == "firefox":
            driver = webdriver.Firefox(executable_path=f"{_driver_path}geckodriver.exe")
        elif _browser == "opera":
            driver = webdriver.Opera(executable_path=f"{_driver_path}operadriver.exe")
        else:
            raise ValueError(f"Browser {_browser} not supported")
    else:
        executor_url = f"http://{_executor}:4444/wd/hub"

        caps = {
            "browserName": _browser,
            # "screenResolution": "1280x720",
            # "name": "Opencart",
            # "selenoid:options": {
            #     "enableVNC": vnc,
            #     "enableVideo": videos,
            #     "enableLog": logs
            # },
            # 'acceptSslCerts': True,
            # 'acceptInsecureCerts': True,
            # 'timeZone': 'Europe/Moscow',
            # 'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
        )

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
