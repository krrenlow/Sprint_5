from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from urls import URLs
import pytest
from selenium.common.exceptions import TimeoutException


class TestUserLogout:
    def test_successful_logout(self, driver):

        try:
            # 1. Переход на базовый URL
            driver.get(URLs.BASE_URL)

            # 2. Авторизация
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN)
            ).click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP)
            )
            driver.find_element(*AuthLocators.LOGIN_EMAIL).send_keys("kr.ren.low@gmail.com")
            driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys("5555")
            driver.find_element(*AuthLocators.LOGIN_SUBMIT_BTN).click()

            # 3. Проверка авторизации
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(AuthLocators.PROFILE_NAME)
            )

            # 4. Выход из системы
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(AuthLocators.AVATAR_ICON)
            ).click()

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)
            ).click()

            # 5. Проверка выхода (альтернативные варианты)
            try:
                # Вариант 1: Ждем появления кнопки входа
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(AuthLocators.ENTER_REGISTER_BTN)
                )

                # Вариант 2: Проверяем, что URL изменился (не обязательно на BASE_URL)
                current_url = driver.current_url
                assert current_url != URLs.PROFILE_URL, \
                    f"После выхода остались на странице профиля: {current_url}"

                # Вариант 3: Проверяем отсутствие элемента профиля
                WebDriverWait(driver, 5).until(
                    EC.invisibility_of_element_located(AuthLocators.PROFILE_NAME)
                )

            except TimeoutException:
                # Если не сработали проверки, делаем скриншот
                driver.save_screenshot("logout_failed.png")
                pytest.fail("Не удалось подтвердить выход из системы")

            # 6. Проверка текста кнопки
            button_text = driver.find_element(*AuthLocators.ENTER_REGISTER_BTN).text.strip()
            assert button_text == "Вход и регистрация", \
                f"Ожидался текст 'Вход и регистрация', получено: '{button_text}'"

        except Exception as e:
            driver.save_screenshot("test_error.png")
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")