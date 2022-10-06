from data.product_data import UserTestData
from pages.registration_user_page import RegistrationPage


def test_add_new_product(driver, url, admin_login):

    """Тест проверяет добавление нового пользователя"""

    registration = RegistrationPage(driver)
    registration.open_registration_page(url)
    user = UserTestData().generate_random_user()
    registration.create_random_user(user)
    assert registration.get_current_url().split("=")[-1] == "account/success"
    assert registration.get_content_title() == "Your Account Has Been Created!"
