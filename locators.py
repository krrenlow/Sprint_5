from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы для авторизации и регистрации"""
    # Основные элементы
    ENTER_REGISTER_BTN = (By.XPATH, "//button[text()='Вход и регистрация']")
    PROFILE_NAME = (By.XPATH, "//h3[@class='profileText name']")
    AVATAR_ICON = (By.CLASS_NAME, "circleSmall")
    LOGOUT_BTN = (By.XPATH, ".//button[text()='Выйти']")

    # Логин попап
    LOGIN_POPUP = (By.XPATH, "//form[@class='popUp_shell__LuyqR']")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN_EMAIL = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_SUBMIT_BTN = (By.XPATH, "//button[text()='Войти']")

    # Регистрация попап
    REGISTER_POPUP = (By.XPATH, "//div[@class='popUp_inputColumn__RgD8n']")
    REGISTER_EMAIL = (By.XPATH, "//input[@name='email']")
    REGISTER_PASSWORD = (By.XPATH, "//input[@name='password']")
    REGISTER_REPEAT_PASSWORD = (By.XPATH, "//input[@name='submitPassword']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")

    # Ошибки
    ERROR_TEXT = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
    ERROR_EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='email']")
    ERROR_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='password']")
    ERROR_REPEAT_PASSWORD_FIELD = (By.XPATH,
                                   "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='submitPassword']")


class AdLocators:
    """Локаторы для работы с объявлениями"""
    CREATE_AD_BTN = (By.XPATH, "//*[text()='Разместить объявление']")
    AUTH_REQUIRED_POPUP = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

    # Создание объявления
    NEW_AD_HEADER = (By.XPATH, "//h1[text()='Новое объявление']")
    AD_NAME_INPUT = (By.XPATH, "//input[@name='name']")
    FILLED_AD_NAME = (By.XPATH, "//input[@value='Гарри Поттер']")
    CATEGORY_DROPDOWN = (By.XPATH, "//div[@class='dropDownMenu_input__itKtw' and .//input[@name='category']]/button")
    BOOKS_CATEGORY = (By.XPATH, "//button[span[text()='Книги']]")
    USED_CONDITION = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']")
    CITY_DROPDOWN = (By.XPATH, "//div[@class='dropDownMenu_input__itKtw' and .//input[@name='city']]/button")
    SPB_CITY = (By.XPATH, "//button[span[text()='Санкт-Петербург']]")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    PUBLISH_BTN = (By.XPATH, "//button[text()='Опубликовать']")
    PUBLISHED_AD = (By.XPATH, "//h2[contains(text(), 'Приключения')]")