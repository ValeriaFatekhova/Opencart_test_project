from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGO = (By.ID, "logo")
    LOGO_LINK = (By.CSS_SELECTOR, "#logo a")
    CART = (By.ID, "cart")
    MENU = (By.ID, "menu")
    MENU_ITEMS = (By.CSS_SELECTOR, "#menu ul.nav>li>a")
    SEARCH = (By.ID, "search")
    CONTENT = (By.ID, "content")
    SLIDESHOW = (By.ID, "slideshow0")
    COMPANIES = (By.ID, "carousel0")
    CURRENCY_BUTTON = (By.ID, "form-currency")
    CURRENCY_VALUE = (By.CSS_SELECTOR, "#form-currency strong")
    EURO = (By.NAME, "EUR")
    POUND = (By.NAME, "GBP")
    USD = (By.NAME, "USD")
    TOTAL_CART = (By.ID, "cart-total")

    MENU_LIST = [
        ("Desktops", "http://localhost/desktops"),
        ("Laptops & Notebooks", "http://localhost/laptop-notebook"),
        ("Components", "http://localhost/component"),
        ("Tablets", "http://localhost/tablet"),
        ("Software", "http://localhost/software"),
        ("Phones & PDAs", "http://localhost/smartphone"),
        ("Cameras", "http://localhost/camera"),
        ("MP3 Players", "http://localhost/mp3-players"),
    ]

    HOME_PAGE_URL = "http://localhost/index.php?route=common/home"

    TIMEOUT_FOR_ELEMENTS = 3

    def open_home_page(self, url):
        self.open_page(url)

    def is_logo(self):
        self.find_element(self.LOGO, self.TIMEOUT_FOR_ELEMENTS)

    def is_search(self):
        self.find_element(self.SEARCH, self.TIMEOUT_FOR_ELEMENTS)

    def is_cart(self):
        self.find_element(self.CART, self.TIMEOUT_FOR_ELEMENTS)

    def is_menu(self):
        self.find_element(self.MENU, self.TIMEOUT_FOR_ELEMENTS)

    def is_content(self):
        self.find_element(self.CONTENT, self.TIMEOUT_FOR_ELEMENTS)

    def is_slideshow(self):
        self.find_element(self.SLIDESHOW, self.TIMEOUT_FOR_ELEMENTS)

    def is_companies(self):
        self.find_element(self.COMPANIES, self.TIMEOUT_FOR_ELEMENTS)

    def check_logo_link(self):
        if self.get_element_link(self.LOGO_LINK, self.TIMEOUT_FOR_ELEMENTS) != self.HOME_PAGE_URL:
            raise AssertionError("Logo link is incorrect")

    def get_menu_items(self):
        return self.find_elements(self.MENU_ITEMS, self.TIMEOUT_FOR_ELEMENTS)

    def check_menu_items(self, elements):
        for i in range(len(elements)):
            temp = (elements[i].text, elements[i].get_attribute("href"))
            if temp != self.MENU_LIST[i]:
                raise AssertionError("Menu items are incorrect")

    def change_currency(self, name):
        self.click(self.CURRENCY_BUTTON, self.TIMEOUT_FOR_ELEMENTS)
        if name == "EUR":
            self.click(self.EURO, self.TIMEOUT_FOR_ELEMENTS)
        elif name == "GBP":
            self.click(self.POUND, self.TIMEOUT_FOR_ELEMENTS)
        elif name == "USD":
            self.click(self.USD, self.TIMEOUT_FOR_ELEMENTS)
        else:
            raise AssertionError(f"Currency {name} is not presented")

    def get_cart_total(self):
        return self.get_text(self.TOTAL_CART, self.TIMEOUT_FOR_ELEMENTS)

    def get_currency(self):
        return self.get_text(self.CURRENCY_VALUE, self.TIMEOUT_FOR_ELEMENTS)
