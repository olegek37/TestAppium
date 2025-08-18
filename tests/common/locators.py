from appium.webdriver.common.appiumby import AppiumBy
import time


class AndroidLocators:
    #Кнопки меню снизу

    # HOME_BUTTON = (AppiumBy.XPATH, "//android.view.View[@resource-id='home']/android.view.View[1]/android.view.View[1]")
    HOME_BUTTON= (AppiumBy.XPATH,"//*[@text='Дом']")
    FAVORITES_BUTTON = (AppiumBy.XPATH,"//*[@text='Избранные']")
    NOTICE_BUTTON = (AppiumBy.XPATH,"//*[@text='Оповещения']")
    SETTINGS_BUTTON = (AppiumBy.XPATH, "//*[@text='Настройки']")

    # Кнопки меню "настройка"
    # ALERT_SETTINGS_BUTTON = (AppiumBy.XPATH,"//*[@text='']")
    COMMON_BUTTON = (AppiumBy.XPATH, "//*[@text='Общие']")
    CONNECTION_BUTTON = (AppiumBy.XPATH, "//*[@text='Соединение']")
    ABOUT_BUTTON = (AppiumBy.XPATH,"//*[@text='О приложении']")

    # Меню "Соединение"
    #поле ввода 
    # KEY_FILED = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='key-field']")
    KEY_FILED = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="key-field"]')
    #поле выбора типа соединения
    CONNECTION_TYPE = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='key-field']")

    #Зона на локальном стенде
    ZONE_LOCAL = (AppiumBy.XPATH, '//android.view.View[@resource-id="sec-floors"]')


class IOSLocators:
    HOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "HomeButton")
    SETTINGS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "SettingsButton")