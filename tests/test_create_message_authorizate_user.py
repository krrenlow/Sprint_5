from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Alllocarots


class TestCreateMessage:

    def test_create_message_authorizate_user(self, login_user):
        driver = login_user

        # Клик на кнопку Разместить объявление
        driver.find_element(*Alllocarots.BUTTON_CREATE_MESSAGE).click()
        # Заполняем поле "Название"
        driver.find_element(*Alllocarots.NAME_MESSAGE).send_keys("Приключения")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(Alllocarots.NAME_MESSAGE, "Приключения"))
        # Ожидание, что поле дропдаун категории кликабельно
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Alllocarots.DROP_DOUN_CATEGORY_BUTTON)))
        # Клик на дропдаун категории
        driver.find_element(*Alllocarots.DROP_DOUN_CATEGORY).click()
        # Ожидание появления выпадающего списка категорий
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Alllocarots.LIST_CATEGORY)))
        # Выбор категории книги
        driver.find_element(*Alllocarots.CATEGORY_BOOKS).click()
        # Переключение на состояние товара Б/У
        driver.find_element(*Alllocarots.B_U).click()
        # Клик на дропдаун города
        driver.find_element(*Alllocarots.CITY_DROP_DOUN).click()
        # Ожидание появления списка городов
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Alllocarots.LIST_CITY)))
        # Клик на город Санкт-Петербург
        driver.find_element(*Alllocarots.CYTI_NAME).click()
        # Ввод описания
        driver.find_element(*Alllocarots.DISCRIPTION).send_keys("Приключения")
        # Клик на ввод стоимости
        driver.find_element(*Alllocarots.PRICE).send_keys(56)
        # Ожидание появляение кнопки Опубликовать
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((Alllocarots.BUTTON_PUBLISH)))
        # Клик на кнопку Опубликовать
        driver.find_element(*Alllocarots.BUTTON_PUBLISH).click()
        # Переход в профиль
        driver.find_element(*Alllocarots.ENTER_TO_PROFILE).click()
        # Ожидание что страница профиля подгрузилась
        WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/profile"))
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((Alllocarots.MESSAGE_PUBLISH_BOOK)))
        assert driver.find_element(*Alllocarots.MESSAGE_PUBLISH_BOOK).is_displayed()