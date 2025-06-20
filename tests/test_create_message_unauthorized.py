from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdLocators
import pytest


class TestCreateAdUnauthorized:
    def test_create_ad_unauthorized(self, driver):

        try:
            # 1. Клик по кнопке создания объявления
            create_ad_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(AdLocators.CREATE_AD_BTN)
            )
            # Прокрутка к элементу перед кликом (если нужно)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", create_ad_btn)
            create_ad_btn.click()

            # 2. Ожидание появления попапа с требованием авторизации
            auth_popup = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(AdLocators.AUTH_REQUIRED_POPUP)
            )

            # 3. Проверка текста сообщения
            popup_text = auth_popup.text.strip()
            expected_text = 'Чтобы разместить объявление, авторизуйтесь'

            assert popup_text == expected_text, \
                f"Ожидаемый текст: '{expected_text}', Фактический: '{popup_text}'"

        except TimeoutException as e:
            driver.save_screenshot("create_ad_timeout_error.png")
            pytest.fail(f"Тест завершился с таймаутом: {str(e)}")
        except Exception as e:
            driver.save_screenshot("create_ad_error.png")
            pytest.fail(f"Неожиданная ошибка: {str(e)}")