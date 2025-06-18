from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots
from helpers import generate_unique_email_not_valid 


class TestNotValidEmail:
    def test_user_not_valid_email(self,driver):
        unique_email_not_valid = generate_unique_email_not_valid() 
        
        # Ждем появления кнопки входа и регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BTN_ENTER_REGISTRATION))
        # Клик по кнопке Вход и регистрация
        driver.find_element(*Alllocarots.BTN_ENTER_REGISTRATION).click()
        
        # Ожидание появления поп-апа входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_ENTER))
        # Клик по кнопке "Нет аккаунта"
        driver.find_element(*Alllocarots.BTN_WITHOUT_ACCOUNT).click()
        
        # Ожидание появления поп-апа регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.POP_UP_REGISTRATION))
        # Ввод почты в поле email не по маске "*******@*******.***"
        driver.find_element(*Alllocarots.INPUT_EMAIL).send_keys(unique_email_not_valid)
        
        # Клик на кнопку создать аккаунт
        driver.find_element(*Alllocarots.CREATE_ACCOUNT).click()
        
        # Ждем появления текста ошибки 
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Alllocarots.TEXT_MISSTAKE)))
        email_error_massege_visible=driver.find_element(*Alllocarots.TEXT_MISSTAKE).is_displayed()
        # Проверка, что поля: Почта, Пароль, Повтор пароля подсвкечиваются красным
        error_fields_visible_red = all([
            driver.find_element(*Alllocarots.EMAIL_RED_BORDER).is_displayed(),
            driver.find_element(*Alllocarots.PASSWORD_RED_BORDER).is_displayed(),
            driver.find_element(*Alllocarots.PASSWORD_REPEAT_RED_BORDER).is_displayed()
        ])

        assert email_error_massege_visible and error_fields_visible_red
