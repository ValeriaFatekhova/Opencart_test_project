from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element {locator} can't be found")

    def find_elements(self, locator, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Elements {locator} can't be found")

    def get_element_link(self, locator, timeout):
        element = self.find_element(locator, timeout)
        return element.get_attribute("href")

    def get_text(self, locator, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text
        except TimeoutException:
            raise AssertionError(f"Elements {locator} can't be found")

    def get_text_element(self, element):
        return element.text

    def click(self, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
        except TimeoutException:
            raise AssertionError(f"Elements {locator} can't be found")

    def click_element(self, element):
        element.click()

    def enter_text_in_field(self, locator, timeout, text):
        try:
            field = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            field.send_keys(text)
        except TimeoutException:
            raise AssertionError(f"Elements {locator} can't be found")

    def accept_alert(self, timeout):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError(f"Alert window is not presented")
        alert.accept()

    def get_current_url(self):
        return self.driver.current_url
