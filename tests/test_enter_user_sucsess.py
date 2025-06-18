from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots
from data import Config



class TestUserAuthentication:
    def test_enter_user_sucsess(self, driver):
        
        # Ждем появления кнопки входа и регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BTN_ENTER_REGISTRATION))
        # Клик по кнопке Вход и регистрация
        driver.find_element(*Alllocarots.BTN_ENTER_REGISTRATION).click()
        # Ожидание появления поп-апа входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_ENTER))
        # Ввод существующей почты в поле email
        driver.find_element(*Alllocarots.INPT_EMAIL).send_keys(Config.ACCOUNT_TWOO)
        # Ввод пароля в поле пароль
        driver.find_element(*Alllocarots.INPT_PASSWORD).send_keys(Config.PASSWORD_ACCOUNT_TWO)
        # Клик на кнопку Войти
        driver.find_element(*Alllocarots.BUTTON_ENTER).click()
        # Ожидание появления имени профиля и аватара пользователя
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.PROFILE_NAME))
        avatar_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Alllocarots.AVATAR_MAIN_PAGE)))
        # Проверка URL и элементов профиля
        expected_url = "https://qa-desk.stand.praktikum-services.ru/login"
        current_url = driver.current_url
        
        assert (current_url == expected_url and 
                driver.find_element(*Alllocarots.PROFILE_NAME).text == "User." and 
                avatar_button.is_displayed())