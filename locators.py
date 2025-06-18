from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Alllocarots():
    #Кнопка входа и регистрации
    BTN_ENTER_REGISTRATION = (By.XPATH, ".//button[text()='Вход и регистрация']")
    #Поп-ап входа с кнопкой "Нет аккаунта"
    POP_UP_ENTER = (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
    #Кнопка нет аккаунта
    BTN_WITHOUT_ACCOUNT = (By.XPATH, '//button[text()="Нет аккаунта"]')
    #Поп-ап окна регистрации после клика на кнопку "Нет аккаунта"
    POP_UP_REGISTRATION = (By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']")
    #Поле ввода почты в по-папе после нажатия на кнопку "Нет аккаунта"
    INPUT_EMAIL = (By.XPATH,".//input[@name='email']")
    #Поле ввода пароля в поп-апе после нажатия на кнопку "Нет аккаунта"
    INPUT_PASSWORD = (By.XPATH,".//input[@name='password']")
    #Повторение пароля в поле ввода, в поп-апе после нажатия на кнопку "Нет аккаунта"
    REPEAT_PASSWORD = (By.XPATH,".//input[@name='submitPassword']")
    # Кнопка создания аккаунта в поп-апе после нажатия на кнопку "Нет аккаунта"
    CREATE_ACCOUNT = (By.XPATH, ".//button[text()='Создать аккаунт']")
    # Шапка профиля созданного юзера на главной стр
    PROFILE_NAME = (By.XPATH, "//h3[@class='profileText name']")
    # Отображение аватарки на главной странице
    AVATAR_MAIN_PAGE = (By.CLASS_NAME, "circleSmall")
    # Текст "Ошибка"
    TEXT_MISSTAKE = (By.XPATH, ".//span[@class='input_span__yWPqB' and text()='Ошибка']")
    # Красная обводка во круг поля Почта
    EMAIL_RED_BORDER = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='email' and @class='input_inputStandart__JweLZ spanGlobal']")
    # Красная обводка во круг поля Пароль
    PASSWORD_RED_BORDER = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='password' and @class='input_inputStandart__JweLZ spanGlobal']")
    # Красная обводка во круг поля Повторите пароль
    PASSWORD_REPEAT_RED_BORDER = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]//input[@name='submitPassword' and @class='input_inputStandart__JweLZ spanGlobal']")
    # Поле ввода для почты в поп-апе Войти
    INPT_EMAIL = (By.XPATH, ".//input[@name='email']")
    # Поле ввода для паролья в поп-апе Войти
    INPT_PASSWORD = (By.XPATH, ".//input[@name='password']")
    # Кнопка войти в поп-апе Войти
    BUTTON_ENTER = (By.XPATH,".//button[text()='Войти']")
    # Кнопка Выйти на главной стр
    BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выйти']")
    # Кнопка Разместить объявление на главной странице
    BUTTON_CREATE_MESSAGE = (By.XPATH, ".//*[text() = 'Разместить объявление']")
    # Поп-ап с текстом "Чтобы разместить объявление, авторизуйтесь"
    POPUP_MESSAGE_AUTHORIZATE = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    # Заголовок страницы создания нового объявления
    CREATE_NEW_MESSAGE = (By.XPATH, ".//h1[text()='Новое объявление']")
    # Поле ввода Названия объявления на стр создания нового объявления
    NAME_MESSAGE = (By.XPATH, ".//input[@name='name']")
    # Проверка, что в поле Название появились данные
    NAME_INPUT_FULL = (By.XPATH, ".//input[@value='Гарри Поттер']")
    # Клик на дропдаун категории
    DROP_DOUN_CATEGORY = (By.XPATH, ".//div[@class='dropDownMenu_input__itKtw' and .//input[@name='category']]/button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    # Поле дропдауна выбора категории
    DROP_DOUN_CATEGORY_BUTTON = (By.XPATH, ".//div[@class='dropDownMenu_input__itKtw' and .//input[@name='category']]/button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    # Выпавший список категорий
    LIST_CATEGORY = (By.XPATH, "//button[contains(@class, 'dropDownMenu_arrowUp__I25Xq')]")
    # Выбор категории Книги
    CATEGORY_BOOKS = (By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']/button[span[text()='Книги']]")
    # Выбор состояния Б/У
    B_U = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']")
    # Клик на кнопку дропдауна города
    CITY_DROP_DOUN = (By.XPATH,".//div[@class='dropDownMenu_input__itKtw' and .//input[@name='city']]/button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    # Список городов
    LIST_CITY = (By.XPATH, ".//div[@class='dropDownMenu_options__CmHmm']")
    # Выбор города Санкт-Петербург
    CYTI_NAME = (By.XPATH, ".//div[@class='dropDownMenu_options__CmHmm']/button[span[text()='Санкт-Петербург']]")
    # Ввод описания
    DISCRIPTION = (By.XPATH, ".//textarea[@name='description']")
    # Ввод стоимости
    PRICE = (By.XPATH, ".//input[@name='price']")
    # Кнопка опубликовать
    BUTTON_PUBLISH = (By.XPATH, ".//button[text()='Опубликовать']")
    # Переход в профиль
    ENTER_TO_PROFILE = (By.XPATH, "//button[contains(@class, 'circleSmall')]")
    # Объявление
    MESSAGE_PUBLISH_BOOK = (By.XPATH, ".//h2[contains(text(), 'Приключения')]")


