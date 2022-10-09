import pytest
from pages.catalog_page import CatalogPage


"""Catalog page tests"""


@pytest.mark.parametrize(
    "add_to_url",
    [
        "component/scanner",
        "component/monitor",
    ]
)
def test_catalog_left_menu(driver, url, add_to_url):
    url = url + add_to_url
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog_page(url)
    catalog_page.is_left_menu()
    active_items = catalog_page.get_active_menu_items()
    expected_items = add_to_url.split("/")
    for i in range(len(expected_items)):
        if expected_items[i].lower() in active_items[i].lower():
            continue
        else:
            raise AssertionError(f"Incorrect active items in left menu")


@pytest.mark.parametrize(
    "add_to_url",
    [
        "component/scanner",
        "component/monitor",
    ]
)
def test_catalog_content(driver, url, add_to_url):
    url = url + add_to_url
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog_page(url)
    catalog_page.is_catalog_content()
    if catalog_page.get_active_menu_items()[-1].find("0") != -1:
        catalog_page.is_catalog_empty()
    else:
        assert str(len(catalog_page.get_products())) in catalog_page.get_active_menu_items()[-1]


@pytest.mark.parametrize(
    "add_to_url",
    [
        "component/scanner",
        "component/monitor",
    ]
)
def test_catalog_breadcrumbs(driver, url, add_to_url):
    url = url + add_to_url
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog_page(url)
    catalog_page.is_breadcrumbs()


@pytest.mark.parametrize(
    "add_to_url",
    [
        "component/scanner",
        "component/monitor",
    ]
)
def test_catalog_continue_button(driver, url, add_to_url):
    url = url + add_to_url
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog_page(url)
    if catalog_page.get_active_menu_items()[-1].find("0") != -1:
        catalog_page.is_continue_button()
    else:
        try:
            catalog_page.is_continue_button()
        except AssertionError:
            pass


@pytest.mark.parametrize(
    "add_to_url",
    [
        "component/scanner",
        "component/monitor",
    ]
)
def test_list_view_button(driver, url, add_to_url):
    url = url + add_to_url
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog_page(url)
    if catalog_page.get_active_menu_items()[-1].find("0") != -1:
        try:
            catalog_page.is_list_view_button()
        except AssertionError:
            pass
    else:
        catalog_page.is_list_view_button()
