from selenium import webdriver
import random
import string
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Alllocarots

@pytest.fixture()
def driver():
    """Создание драйвера Chrome и его закрытие после завершения тестов."""
    print("driver")
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()



@pytest.fixture
def login_user(driver):
    """Фикстура: логин авторизованного пользователя"""
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    # Ждем появления кнопки входа и регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BTN_ENTER_REGISTRATION))
    # Клик по кнопке Вход и регистрация
    driver.find_element(*Alllocarots.BTN_ENTER_REGISTRATION).click()
    # Ожидание появления поп-апа входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_ENTER))
    # Ввод существующей почты в поле email
    driver.find_element(*Alllocarots.INPT_EMAIL).send_keys("kr.ren.low@gmail.com")
    # Ввод пароля в поле пароль
    driver.find_element(*Alllocarots.INPT_PASSWORD).send_keys("558852")
    # Клик на кнопку Войти
    driver.find_element(*Alllocarots.BUTTON_ENTER).click()
    # Ожидание появления имени профиля и аватара пользователя
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.PROFILE_NAME))

    return driver



