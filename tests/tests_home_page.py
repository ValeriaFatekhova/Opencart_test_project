from pages.home_page import HomePage


"""Home page tests"""


def test_home_page_logo(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_logo()
    home_page.check_logo_link()


def test_home_page_menu(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_menu()
    home_page.check_menu_items(home_page.get_menu_items())


def test_home_page_search(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_search()


def test_home_page_cart(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_cart()


def test_home_page_slideshow(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_slideshow()


def test_home_page_content(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_content()


def test_currency_euro(driver, url):

    """Тест проверяет смену текущей валюты на евро"""

    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.change_currency("EUR")
    assert home_page.get_currency() == "€"
    assert home_page.get_cart_total()[-1] == "€"


def test_currency_pound_sterling(driver, url):

    """Тест проверяет смену текущей валюты на фунт стерлинг"""

    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.change_currency("GBP")
    assert home_page.get_currency() == "£"
    assert "£" in home_page.get_cart_total()


def test_currency_usd(driver, url):

    """Тест проверяет смену текущей валюты на доллар"""

    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.change_currency("USD")
    assert home_page.get_currency() == "$"
    assert "$" in home_page.get_cart_total()
