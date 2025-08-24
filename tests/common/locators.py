from appium.webdriver.common.appiumby import AppiumBy
import time


class AndroidLocators:
    #Кнопки меню снизу

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
    #поле ввода пароля
    KEY_FILED = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="key-field"]')
    #поле выбора типа соединения
    CONNECTION_TYPE = (AppiumBy.XPATH, '//android.view.View[@resource-id="settings-tab-wrapper"]/android.view.View[3]')
    # CONNECTION_TYPE_HOME = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]')
    # CONNECTION_TYPE_AUTO = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[3]/android.view.View/android.view.View[4]')
    # CONNECTION_TYPE_INTERNET = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]')
    CONNECTION_TYPE_HOME = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]//*[@text="Дома"]')
    CONNECTION_TYPE_AUTO = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]//*[@text="Авто"]')
    CONNECTION_TYPE_INTERNET = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]//*[@text="Через интернет"]')


    # LIVING_ROOM = (AppiumBy.XPATH, "//android.view.View[@resource-id="sec-floors"]/android.view.View[1]/android.view.View[1]")
    SENSORS_PANEL_ID = (AppiumBy.XPATH, '//android.view.View[@resource-id="app"]')

    #Зона на локальном стенде
    ZONE_LOCAL = (AppiumBy.XPATH, '//android.view.View[@resource-id="sec-floors"]')


class IOSLocators:
    HOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "HomeButton")
    SETTINGS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "SettingsButton")