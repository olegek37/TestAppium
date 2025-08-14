import pytest
from tests.common.helpers import take_screenshot
from tests.common.locators import AndroidLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time


@pytest.mark.android
class TestHomeScreen:
    def test_demostand(self, driver):
        """Тест проверяет авторизацию на демо-стенде"""
        try:
            home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
            home_button.click()
            settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
            settings_button.click()
            connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
            connection_button.click()
            # driver.back()
            time.sleep(1)
            key_field = driver.find_element(*AndroidLocators.KEY_FILED)
            key_field.clear()
            key_field.send_keys("1212121212121212")
            # key_field.send_keys("121212145454212121214")
            home_button.click()
            time.sleep(10)
            take_screenshot(driver,"stand_auto")
            # проверки после клика
            assert "Гостиная" in driver.page_source, "Не прошла авторизация на демо-стенде"
            
        except Exception as e:
            take_screenshot(driver, "ошибка авторизации")
            pytest.fail(f"ошибка авторизации: {str(e)}")