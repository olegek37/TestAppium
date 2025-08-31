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
    SENSORS_PANEL_ID = (AppiumBy.XPATH, '//android.view.View[@resource-id="roomSensors"]')

    #Зона на локальном стенде
    ZONE_LOCAL = (AppiumBy.XPATH, '//android.view.View[@resource-id="sec-floors"]')


class IOSLocators:
    #-------- Меню нижние кнопки
    HOME_BUTTON = (AppiumBy.NAME, "Дом")
    SETTINGS_BUTTON = (AppiumBy.NAME, "Настройки")
    FAVORITES_BUTTON = (AppiumBy.NAME, "Избранные")
    NOTICE_BUTTON = (AppiumBy.NAME, "Оповещения")

    #-------- Меню Настройки
    COMMON_BUTTON = (AppiumBy.NAME, "Общие")
    CONNECTION_BUTTON = (AppiumBy.NAME, "Соединение")
    NOTIFY_BUTTON = (AppiumBy.NAME, "Оповещения")
    ABOUT_BUTTON = (AppiumBy.NAME, "О приложении")


    CONNECTION_TYPE_SELECT = (AppiumBy.NAME, "Соединение")
    KEY_FILED = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField')
    CONNECT_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="СОЕДИНЕНИЕ"]')

    MIMI = (AppiumBy.ACCESSIBILITY_ID, "mimismart_webapp")
    ZONE_LOCAL = (AppiumBy.ACCESSIBILITY_ID, "Setup")
    PHOTO_CH_NOTIFY = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Фото успешно заменено"]')
    PHONE_GALLERY = (AppiumBy.ACCESSIBILITY_ID, "ГАЛЕРЕЯ ТЕЛЕФОНА")
    PHONE_GALLERY_LAYOUT = (AppiumBy.ACCESSIBILITY_ID,"PXGGridLayout-Group")
    LAMP_3 = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lamp 3"]')

    # Верхнее меню
    MENU_LIGHTING = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Освещение"]')
    MENU_SCENARIOS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Сценарии"]')
    MENU_CURTAINS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Шторы"]')
    MENU_CLIMATE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Климат"]')
    MENU_SECURITY = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Защита"]')
    MENU_SENSORS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Датчики"]')
    MENU_OTHER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Прочие"]')
    MENU_MUSIC = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Музыка"]')


    ALL_ON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Включить всё"]')
    ALL_OFF = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Выключить все"]')

    THEME_NENU = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Тема"]')
    DARK_THEME = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Тёмная"]')

    BACKGROUND_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Фон приложения"]')