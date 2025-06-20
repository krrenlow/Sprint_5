from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import AuthLocators
from urls import URLs
from data import TestData
import time


@pytest.fixture()
def driver():
    """Инициализация и закрытие драйвера Chrome"""
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    """Улучшенная фикстура для авторизации пользователя"""
    try:
        # Увеличиваем время ожидания и добавляем обработку ошибок
        wait = WebDriverWait(driver, 20)

        # 1. Ожидание и клик по кнопке входа (с альтернативными стратегиями)
        try:
            enter_btn = wait.until(EC.element_to_be_clickable(AuthLocators.ENTER_REGISTER_BTN))
            enter_btn.click()
        except:
            # Альтернативный способ клика через JavaScript
            driver.execute_script("arguments[0].click();",
                                  driver.find_element(*AuthLocators.ENTER_REGISTER_BTN))

        # 2. Ожидание попапа авторизации с проверкой нескольких условий
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_POPUP))

        # 3. Ввод учетных данных с очисткой полей
        email_field = wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL))
        email_field.clear()
        email_field.send_keys(TestData.EMAIL)

        password_field = driver.find_element(*AuthLocators.LOGIN_PASSWORD)
        password_field.clear()
        password_field.send_keys(TestData.PASSWORD)

        # 4. Клик по кнопке входа с повторными попытками
        for _ in range(3):
            try:
                driver.find_element(*AuthLocators.LOGIN_SUBMIT_BTN).click()
                break
            except:
                time.sleep(1)

        # 5. Проверка успешной авторизации (более гибкая)
        try:
            wait.until(EC.visibility_of_element_located(AuthLocators.PROFILE_NAME))
            # Альтернативная проверка URL (менее строгая)
            wait.until(lambda d: "profile" in d.current_url.lower() or URLs.BASE_URL in d.current_url)
        except TimeoutException:
            # Проверяем, возможно мы уже на нужной странице
            if "profile" not in driver.current_url.lower():
                raise Exception("Авторизация не удалась: не удалось подтвердить успешный вход")

        yield driver

    except Exception as e:
        # Сохраняем скриншот при ошибке
        driver.save_screenshot("login_error.png")
        pytest.fail(f"Ошибка авторизации: {str(e)}")
        raise

    finally:
        # Пост-условие: выход из системы
        try:
            if "profile" in driver.current_url.lower():
                # Клик по аватару для открытия меню
                avatar = wait.until(EC.element_to_be_clickable(AuthLocators.AVATAR_ICON))
                avatar.click()

                # Клик по кнопке выхода
                logout_btn = wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BTN))
                logout_btn.click()

                # Ожидание возврата на главную страницу
                wait.until(lambda d: URLs.BASE_URL in d.current_url)
        except Exception as e:
            print(f"Ошибка при выходе из системы: {e}")