import pytest
from tests.common.helpers import take_screenshot
from tests.common.locators import AndroidLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time


@pytest.mark.android
class TestHomeScreen:
    def test_demostand(self, driver):
        """Тест проверяет авторизацию на демо-стенде"""
        try:
    
            settings_button = WebDriverWait(driver, 10).until(lambda d: d.find_element(*AndroidLocators.SETTINGS_BUTTON))
            settings_button.click()
            
            # ТОЛЬКО теперь ищем "Соединение" (после перехода на новый экран)
            connection_button = WebDriverWait(driver, 10).until(lambda d: d.find_element(*AndroidLocators.CONNECTION_BUTTON))
            connection_button.click()
            
            # Возвращаемся на главный экран (пример)
            driver.back()
            
            # Работаем с остальными кнопками
            home_button = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(*AndroidLocators.HOME_BUTTON)
            )
            favorites_button = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(*AndroidLocators.FAVORITES_BUTTON)
            )
            notice_button = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(*AndroidLocators.NOTICE_BUTTON)
            )














            # проверки после клика
            assert "Избранные" in driver.page_source, "Не произошел переход после клика"
            
        except Exception as e:
            take_screenshot(driver, "home_button_error")
            pytest.fail(f"Home button test failed: {str(e)}")