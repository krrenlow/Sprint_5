from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from locators import AuthLocators, AdLocators
from urls import URLs
import time


class TestCreateMessage:
    def test_create_message_authorizate_user(self, driver, login_user):
        """
        Улучшенный тест создания объявления с авторизацией пользователя
        """
        wait = WebDriverWait(driver, 20)

        try:
            # 1. Клик на кнопку "Разместить объявление" с обработкой исключений
            self._safe_click(wait, AdLocators.CREATE_AD_BTN)

            # 2. Проверка формы создания объявления
            wait.until(EC.visibility_of_element_located(AdLocators.NEW_AD_HEADER))

            # 3. Заполнение данных объявления
            ad_title = "Приключения"
            self._safe_send_keys(wait, AdLocators.AD_NAME_INPUT, ad_title)
            wait.until(EC.text_to_be_present_in_element_value(AdLocators.AD_NAME_INPUT, ad_title))

            # 4. Выбор категории
            self._safe_click(wait, AdLocators.CATEGORY_DROPDOWN)
            self._safe_click(wait, AdLocators.BOOKS_CATEGORY)

            # 5. Установка состояния товара
            self._safe_click(wait, AdLocators.USED_CONDITION)

            # 6. Выбор города
            self._safe_click(wait, AdLocators.CITY_DROPDOWN)
            self._safe_click(wait, AdLocators.SPB_CITY)

            # 7. Заполнение остальных полей
            self._safe_send_keys(wait, AdLocators.DESCRIPTION_INPUT, "Книга в отличном состоянии")
            self._safe_send_keys(wait, AdLocators.PRICE_INPUT, "560")

            # 8. Публикация объявления
            self._safe_click(wait, AdLocators.PUBLISH_BTN)

            # 9. Переход в профиль с обработкой StaleElement
            self._safe_click_with_retry(wait, AuthLocators.AVATAR_ICON, retries=3, delay=1)

            # 10. Проверка объявления в профиле
            wait.until(lambda d: URLs.PROFILE_URL in d.current_url)
            published_ad = self._wait_for_stable_element(wait, AdLocators.PUBLISHED_AD)
            assert ad_title in published_ad.text, "Название объявления не соответствует ожидаемому"

        except Exception as e:
            driver.save_screenshot("test_failure.png")
            raise

    def _safe_click(self, wait, locator):
        """Безопасный клик с обработкой исключений"""
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except StaleElementReferenceException:
            # Если элемент устарел, находим его заново
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def _safe_send_keys(self, wait, locator, text):
        """Безопасный ввод текста"""
        element = wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def _safe_click_with_retry(self, wait, locator, retries=3, delay=1):
        """Клик с повторными попытками"""
        for attempt in range(retries):
            try:
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except Exception as e:
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
                continue

    def _wait_for_stable_element(self, wait, locator, attempts=3, delay=1):
        """Ожидание стабильного элемента"""
        for _ in range(attempts):
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                # Дополнительная проверка, что элемент не меняется
                time.sleep(delay)
                if element.is_displayed():
                    return element
            except StaleElementReferenceException:
                continue
        raise TimeoutError(f"Элемент {locator} не стабилизировался после {attempts} попыток")