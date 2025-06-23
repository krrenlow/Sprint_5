from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdLocators
import pytest


class TestCreateAdUnauthorized:
    def test_create_ad_unauthorized(self, driver):

        wait = WebDriverWait(driver, 15)

        # 1. Клик по кнопке создания объявления
        create_ad_btn = wait.until(EC.element_to_be_clickable(AdLocators.CREATE_AD_BTN))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", create_ad_btn)
        create_ad_btn.click()

        # 2. Проверка появления попапа авторизации
        auth_popup = wait.until(EC.visibility_of_element_located(AdLocators.AUTH_REQUIRED_POPUP))

        # 3. Проверка текста сообщения
        expected_text = 'Чтобы разместить объявление, авторизуйтесь'
        assert auth_popup.text.strip() == expected_text, \
            f"Текст в попапе не соответствует ожидаемому. Ожидалось: '{expected_text}', получено: '{auth_popup.text.strip()}'"