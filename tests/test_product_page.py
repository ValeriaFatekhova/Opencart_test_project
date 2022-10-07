import allure
import pytest
from pages.product_page import ProductPage


"""Product page tests"""


@pytest.mark.parametrize(
    "add_to_url",
    [
        "monitor/test",
        "laptop-notebook/hp-lp3065",
    ]
)
@allure.feature('Страница товара')
@allure.title("Проверка наличия фото товара на странице товара")
def test_product_thumbnails(driver, url, add_to_url):
    url = url + add_to_url
    product_page = ProductPage(driver)
    product_page.open_product_page(url)
    product_page.is_thumbnails()


@pytest.mark.parametrize(
    "add_to_url",
    [
        "monitor/test",
        "laptop-notebook/hp-lp3065",
    ]
)
@allure.feature('Страница товара')
@allure.title("Проверка наличия описания товара на странице товара")
def test_product_description(driver, url, add_to_url):
    url = url + add_to_url
    product_page = ProductPage(driver)
    product_page.open_product_page(url)
    product_page.is_product_description()


@pytest.mark.parametrize(
    "add_to_url",
    [
        "monitor/test",
        "laptop-notebook/hp-lp3065",
    ]
)
@allure.feature('Страница товара')
@allure.title("Проверка наличия отзывов о товаре на странице товара")
def test_product_review(driver, url, add_to_url):
    url = url + add_to_url
    product_page = ProductPage(driver)
    product_page.open_product_page(url)
    product_page.is_product_review()


@pytest.mark.parametrize(
    "add_to_url",
    [
        "monitor/test",
        "laptop-notebook/hp-lp3065",
    ]
)
@allure.feature('Страница товара')
@allure.title("Проверка наличия кнопки 'Добавить в корзину' на странице товара")
def test_add_to_cart_button(driver, url, add_to_url):
    url = url + add_to_url
    product_page = ProductPage(driver)
    product_page.open_product_page(url)
    product_page.is_add_to_cart_button()


@pytest.mark.parametrize(
    "add_to_url",
    [
        "monitor/test",
        "laptop-notebook/hp-lp3065",
    ]
)
@allure.feature('Страница товара')
@allure.title("Проверка наличия рейтинга товара на странице товара")
def test_product_rating(driver, url, add_to_url):
    url = url + add_to_url
    product_page = ProductPage(driver)
    product_page.open_product_page(url)
    product_page.is_rating()
