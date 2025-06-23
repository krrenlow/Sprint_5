from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators, AdLocators
from urls import URLs
import pytest


class TestCreateMessage:
    def test_create_message_authorizate_user(self, driver, login_user):
        """
        Тест создания объявления с авторизацией пользователя
        Без обработчиков ошибок и скриншотов - они должны быть вынесены в фикстуры
        """
        wait = WebDriverWait(driver, 10)

        # 1. Клик на кнопку "Разместить объявление"
        create_ad_btn = wait.until(EC.element_to_be_clickable(AdLocators.CREATE_AD_BTN))
        create_ad_btn.click()

        # 2. Проверка формы создания объявления
        wait.until(EC.visibility_of_element_located(AdLocators.NEW_AD_HEADER))

        # 3. Заполнение данных объявления
        ad_title = "Приключения"
        name_input = wait.until(EC.visibility_of_element_located(AdLocators.AD_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(ad_title)

        # 4. Выбор категории
        category_dropdown = wait.until(EC.element_to_be_clickable(AdLocators.CATEGORY_DROPDOWN))
        category_dropdown.click()

        books_category = wait.until(EC.element_to_be_clickable(AdLocators.BOOKS_CATEGORY))
        books_category.click()

        # 5. Установка состояния товара
        used_condition = wait.until(EC.element_to_be_clickable(AdLocators.USED_CONDITION))
        used_condition.click()

        # 6. Выбор города
        city_dropdown = wait.until(EC.element_to_be_clickable(AdLocators.CITY_DROPDOWN))
        city_dropdown.click()

        spb_city = wait.until(EC.element_to_be_clickable(AdLocators.SPB_CITY))
        spb_city.click()

        # 7. Заполнение остальных полей
        description_input = wait.until(EC.visibility_of_element_located(AdLocators.DESCRIPTION_INPUT))
        description_input.send_keys("Книга в отличном состоянии")

        price_input = wait.until(EC.visibility_of_element_located(AdLocators.PRICE_INPUT))
        price_input.send_keys("560")

        # 8. Публикация объявления
        publish_btn = wait.until(EC.element_to_be_clickable(AdLocators.PUBLISH_BTN))
        publish_btn.click()

        # 9. Переход в профиль
        avatar_icon = wait.until(EC.element_to_be_clickable(AuthLocators.AVATAR_ICON))
        avatar_icon.click()

        # 10. Проверка объявления в профиле
        wait.until(lambda d: URLs.PROFILE_URL in d.current_url)

        published_ad = wait.until(EC.visibility_of_element_located(AdLocators.PUBLISHED_AD))
        assert ad_title in published_ad.text, "Название объявления не соответствует ожидаемому"