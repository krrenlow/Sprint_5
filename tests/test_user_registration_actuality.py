from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from data import Config
import pytest
import time


class TestActualityUser:
    def test_user_registration_actuality(self, driver):

        try:
            # 1. Открытие формы регистрации
            WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN)
            ).click()

            WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP)
            )

            # Переход к форме регистрации
            driver.find_element(*AuthLocators.NO_ACCOUNT_BTN).click()

            # 2. Заполнение формы регистрации
            WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.REGISTER_POPUP)
            )

            # Ввод данных существующего аккаунта
            email_field = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.REGISTER_EMAIL)
            )
            email_field.clear()
            email_field.send_keys(Config.ACCOUNT_EMAIL)

            password_field = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.REGISTER_PASSWORD)
            )
            password_field.clear()
            password_field.send_keys(Config.ACCOUNT_PASSWORD)

            repeat_password_field = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.REGISTER_REPEAT_PASSWORD)
            )
            repeat_password_field.clear()
            repeat_password_field.send_keys(Config.ACCOUNT_PASSWORD)

            # 3. Отправка формы
            driver.find_element(*AuthLocators.CREATE_ACCOUNT_BTN).click()

            # 4. Проверка ошибок валидации
            error_text = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.ERROR_TEXT)
            )

            # Проверка подсветки полей с ошибками
            error_fields = [
                AuthLocators.ERROR_EMAIL_FIELD,
                AuthLocators.ERROR_PASSWORD_FIELD,
                AuthLocators.ERROR_REPEAT_PASSWORD_FIELD
            ]

            errors_displayed = all(
                driver.find_element(*field).is_displayed()
                for field in error_fields
            )

            # 5. Проверки
            assert error_text.is_displayed(), "Сообщение об ошибке не отображается"
            assert errors_displayed, "Не все поля с ошибками подсвечены"

        except Exception as e:
            driver.save_screenshot(f"registration_validation_error_{time.strftime('%Y%m%d_%H%M%S')}.png")
            pytest.fail(f"Ошибка при проверке валидации регистрации: {str(e)}")