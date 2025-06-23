from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from urls import URLs
from data import TestData


@pytest.fixture()
def driver():
    """Инициализация и закрытие драйвера Chrome"""
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    """Фикстура для авторизации пользователя"""
    wait = WebDriverWait(driver, 10)

    # Открытие попапа авторизации
    enter_btn = wait.until(EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN))
    enter_btn.click()

    # Ожидание появления попапа
    wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP))

    # Ввод учетных данных
    email_field = wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL))
    email_field.clear()
    email_field.send_keys(TestData.EMAIL)

    password_field = wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_PASSWORD))
    password_field.clear()
    password_field.send_keys(TestData.PASSWORD)

    # Отправка формы
    submit_btn = wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BTN))
    submit_btn.click()

    # Проверка успешной авторизации
    wait.until(EC.visibility_of_element_located(AuthLocators.PROFILE_NAME))

    yield driver