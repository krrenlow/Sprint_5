from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from data import Config
from urls import URLs
import pytest

class TestUserAuthentication:
    def test_successful_login(self, driver):

        # 1. Открываем главную страницу
        driver.get(URLs.BASE_URL)

        # 2. Открываем форму входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN)
        ).click()

        # 3. Ожидаем появление попапа авторизации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP)
        )

        # 4. Вводим учетные данные
        driver.find_element(*AuthLocators.LOGIN_EMAIL).send_keys(Config.ACCOUNT_EMAIL)
        driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys(Config.ACCOUNT_PASSWORD)
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BTN).click()

        # 5. Проверяем успешную авторизацию
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.PROFILE_NAME)
        )

        # Проверяем отображение аватара
        avatar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.AVATAR_ICON)
        )

        # Проверяем имя пользователя и отображение аватара
        profile_name = driver.find_element(*AuthLocators.PROFILE_NAME).text
        assert profile_name == "User.", f"Неверное имя пользователя: {profile_name}"
        assert avatar.is_displayed(), "Аватар не отображается"