from data.product_data import ProductTestData
from pages.adm_products_list_page import AdmProductsListPage


def test_add_new_product(driver, url, admin_login):

    """Тест проверяет добавление нового товара в админском разделе сайта"""

    adm_products = AdmProductsListPage(driver)
    adm_products.open_adm_products_list_page()
    product = ProductTestData().generate_random_product()
    num1 = adm_products.get_num_of_products()
    adm_products.create_new_product(product)
    num2 = adm_products.get_num_of_products()
    assert num2-num1 == 1
    assert adm_products.is_new_product(product)


def test_delete_first_product(driver, url, admin_login):

    """Тест проверяет удаление первого товара на первой странице списка товаров в админском разделе"""

    adm_products = AdmProductsListPage(driver)
    adm_products.open_adm_products_list_page()
    num1 = adm_products.get_num_of_products()
    adm_products.delete_first_product()
    num2 = adm_products.get_num_of_products()
    assert num1 - num2 == 1

