from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots
from helpers import generate_unique_email_valid
from data import Config

class TestFirstRregistration:

    def test_user_registration_sucsess(self,driver):
        unique_email_valid = generate_unique_email_valid()
        # Ждем появления кнопки входа и регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BTN_ENTER_REGISTRATION))
        # Клик по кнопке Входи и регистрация
        driver.find_element(*Alllocarots.BTN_ENTER_REGISTRATION).click()
        # Ожидание появления поп-апа входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_ENTER))
        # Клик по кнопке "Нет аккаунта"
        driver.find_element(*Alllocarots.BTN_WITHOUT_ACCOUNT).click()
        # Ожидание появления поп-апа регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_REGISTRATION))
        # Ввод почты в поле email
        driver.find_element(*Alllocarots.INPUT_EMAIL).send_keys(unique_email_valid)
        # Ввод пароля в поле пароль
        driver.find_element(*Alllocarots.INPUT_PASSWORD).send_keys(Config.PASSWORD)
        # Повторный ввод пароля в поле повторить пароль
        driver.find_element(*Alllocarots.REPEAT_PASSWORD).send_keys(Config.PASSWORD)
        # Клик на кнопку создать аккаунт
        driver.find_element(*Alllocarots.CREATE_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.PROFILE_NAME))
        # Ожидание появления имени профиля и аватара пользователя
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.PROFILE_NAME))
        avatar_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Alllocarots.AVATAR_MAIN_PAGE)))
        # Проверка URL и элементов профиля
        expected_url = "https://qa-desk.stand.praktikum-services.ru/regiatration"
        current_url = driver.current_url
        
        assert (current_url == expected_url and 
                driver.find_element(*Alllocarots.PROFILE_NAME).text == "User." and 
                avatar_button.is_displayed())
        