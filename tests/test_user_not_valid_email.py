from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from helpers import generate_unique_email_not_valid


class TestNotValidEmail:

    def test_user_not_valid_email(self, driver):
        unique_email_not_valid = generate_unique_email_not_valid()

        # Ожидание и клик по кнопке входа и регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.ENTER_REGISTER_BTN)
        ).click()

        # Ожидание появления попапа входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP)
        )

        # Клик по кнопке "Нет аккаунта"
        driver.find_element(*AuthLocators.NO_ACCOUNT_BTN).click()

        # Ожидание появления попапа регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.REGISTER_POPUP)
        )

        # Ввод невалидного email
        driver.find_element(*AuthLocators.REGISTER_EMAIL).send_keys(unique_email_not_valid)

        # Клик по кнопке создания аккаунта
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()

        # Ожидание появления сообщения об ошибке
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.ERROR_TEXT)
        )

        # Проверка отображения сообщения об ошибке
        error_message_visible = driver.find_element(*AuthLocators.ERROR_TEXT).is_displayed()

        # Проверка подсветки полей с ошибками
        fields_with_errors = [
            AuthLocators.ERROR_EMAIL_FIELD,
            AuthLocators.ERROR_PASSWORD_FIELD,
            AuthLocators.ERROR_REPEAT_PASSWORD_FIELD
        ]

        error_fields_visible = all(
            driver.find_element(*field).is_displayed()
            for field in fields_with_errors
        )

        # Проверки с информативными сообщениями
        assert error_message_visible, "Сообщение об ошибке не отображается"
        assert error_fields_visible, "Не все поля с ошибками подсвечены"