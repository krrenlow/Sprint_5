from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots




class TestUserAuthentication:
    def test_enter_user_sucsess(self, driver, login_user):
        driver = login_user
        #Разлогиниваемся из аккаунта
        driver.find_element(*Alllocarots.BUTTON_LOGOUT).click()
        #Ожидаем появление кнопки Вход и Регистрация
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BTN_ENTER_REGISTRATION))
        
        assert driver.find_element(*Alllocarots.BTN_ENTER_REGISTRATION).text == "Вход и регистрация"