import allure
import pytest
from pages.home_page import HomePage

"""Home page tests"""

@allure.feature('Домашняя страница')
@allure.title("Проверка логотипа на главной странице")
def test_home_page_logo(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_logo()
    home_page.check_logo_link()


@allure.feature('Домашняя страница')
@allure.title("Проверка наличия меню на главной странице")
def test_home_page_menu(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_menu()
    home_page.check_menu_items(home_page.get_menu_items())


@allure.feature('Домашняя страница')
@allure.title("Проверка наличия поиска на главной странице")
def test_home_page_search(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_search()


@allure.feature('Домашняя страница')
@allure.title("Проверка наличия корзины на главной странице")
def test_home_page_cart(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_cart()


@allure.feature('Домашняя страница')
@allure.title("Проверка наличия слайдшоу товаров на главной странице")
def test_home_page_slideshow(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_slideshow()


@allure.feature('Домашняя страница')
@allure.title("Проверка наличия списка товаров на главной странице")
def test_home_page_content(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_content()


@pytest.mark.parametrize(
    "currency, symbol",
    [
        ("EUR", "€"),
        ("GBP", "£"),
        ("USD", "$"),
    ])
@allure.feature('Домашняя страница')
@allure.title("Проверка смены валюты на главной странице")
def test_currency(driver, url, currency, symbol):
    """Тест проверяет смену текущей валюты"""

    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.change_currency(currency)
    assert home_page.get_currency() == symbol
    assert symbol in home_page.get_cart_total()
