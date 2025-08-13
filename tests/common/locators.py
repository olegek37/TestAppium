from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction
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





class IOSLocators:
    HOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "HomeButton")
    SETTINGS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "SettingsButton")