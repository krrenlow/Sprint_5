from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots
import pytest



class TestCreateMessageUnauthorized:

    def test_create_message_unauthorized(self,driver):
        # Ждем появления кнопки Разместить объявление
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BUTTON_CREATE_MESSAGE))
        # Клик по кнопке Разместить объявление
        driver.find_element(*Alllocarots.BUTTON_CREATE_MESSAGE).click()
        # Ждем появление поп-апа "Чтобы разместить объявление, авторизуйтесь"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Alllocarots.BUTTON_CREATE_MESSAGE))
        # Получение попа-апа и текста в нем
        message_need_authoriate = driver.find_element(*Alllocarots.POPUP_MESSAGE_AUTHORIZATE).text

        assert  message_need_authoriate == 'Чтобы разместить объявление, авторизуйтесь'