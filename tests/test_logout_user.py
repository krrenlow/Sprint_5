from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from urls import URLs
import pytest


class TestUserLogout:
    def test_successful_logout(self, driver):

        wait = WebDriverWait(driver, 10)

        # 1. Авторизация
        driver.get(URLs.BASE_URL)
        wait.until(EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP))

        driver.find_element(*AuthLocators.LOGIN_EMAIL).send_keys("kr.ren.low@gmail.com")
        driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys("5555")
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BTN).click()

        # 2. Проверка успешной авторизации
        wait.until(EC.visibility_of_element_located(AuthLocators.PROFILE_NAME))

        # 3. Выход из системы
        wait.until(EC.element_to_be_clickable(AuthLocators.AVATAR_ICON)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN)).click()

        # 4. Проверки после выхода
        enter_btn = wait.until(EC.visibility_of_element_located(AuthLocators.ENTER_REGISTER_BTN))
        assert enter_btn.text.strip() == "Вход и регистрация", "Неверный текст кнопки после выхода"

        assert URLs.BASE_URL in driver.current_url, "Неверный URL после выхода"
        assert len(driver.find_elements(*AuthLocators.PROFILE_NAME)) == 0, "Элемент профиля остался на странице"