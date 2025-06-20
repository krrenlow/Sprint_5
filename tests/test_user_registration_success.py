from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from helpers import generate_unique_email_valid
from data import Config
from urls import URLs
import pytest
import time


class TestFirstRegistration:

    def test_user_registration_success(self, driver):

        unique_email_valid = generate_unique_email_valid()
        screenshots_enabled = True  # Флаг для включения/выключения скриншотов

        try:
            # 1. Открытие формы регистрации
            register_btn = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN)
            )
            register_btn.click()

            # Ждем форму входа
            WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP)
            )

            # Переход к регистрации
            no_account_btn = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)
            )
            no_account_btn.click()

            # 2. Заполнение формы регистрации
            WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.REGISTER_POPUP)
            )

            # Находим элементы формы каждый раз перед взаимодействием
            def safe_send_keys(locator, text):
                element = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                    EC.element_to_be_clickable(locator)
                )
                element.clear()
                element.send_keys(text)

            # Ввод данных
            safe_send_keys(AuthLocators.REGISTER_EMAIL, unique_email_valid)
            safe_send_keys(AuthLocators.REGISTER_PASSWORD, Config.ACCOUNT_PASSWORD)
            safe_send_keys(AuthLocators.REGISTER_REPEAT_PASSWORD, Config.ACCOUNT_PASSWORD)

            # 3. Отправка формы
            submit_btn = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(AuthLocators.CREATE_ACCOUNT_BTN)
            )
            submit_btn.click()

            # 4. Проверка успешной регистрации
            WebDriverWait(driver, 20).until(
                lambda d: URLs.PROFILE_URL in d.current_url or
                          URLs.BASE_URL in d.current_url
            )

            # Проверка элементов профиля
            profile_name = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.PROFILE_NAME)
            )

            avatar = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(AuthLocators.AVATAR_ICON)
            )

            # 5. Проверки
            assert profile_name.text == "User.", \
                f"Ожидалось имя профиля: 'User.', получено: '{profile_name.text}'"

            assert avatar.is_displayed(), "Аватар пользователя не отображается"

        except Exception as e:
            if screenshots_enabled:
                timestamp = time.strftime('%Y%m%d_%H%M%S')
                driver.save_screenshot(f"registration_error_{timestamp}.png")
            pytest.fail(f"Ошибка при регистрации: {str(e)}\nURL: {driver.current_url}")