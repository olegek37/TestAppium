import pytest
from tests.common.helpers import *
# from tests.common.helpers import take_screenshot
# from tests.common.helpers import check_network_connection
from tests.common.locators import AndroidLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.android

class TestGeneral:
    def test_cold_start(self, driver):
        """Проверка холодного старта приложения"""
        main_screen = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "sec-floors")))
        assert main_screen.is_displayed(), "Главный экран не отображается после холодного старта"
        
    def test_hot_start(self, driver):
        """Проверка горячего старта приложения"""
        driver.background_app(-1)
        main_screen = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "sec-floors")))
        assert main_screen.is_displayed(), "Главный экран не отображается после горячего старта"
    
    # def test_interruptions(self, driver):
    #     """Реакция на прерывания"""
    #     driver.start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        
    #     driver.start_activity("com.mimismart.app", "your.app.MainActivity")
    #     main_screen = driver.find_element(AppiumBy.ID, "sec-floors")
    #     assert main_screen.is_displayed(), "Главный экран не отображается после прерывания"

    def test_interruptions(self, driver):
        
        """Реакция на прерывания"""  
        # Получаем текущий пакет приложения
        current_package = driver.current_package
        
        # Переключаемся на контакты (прерывание)
        # driver.execute_script('mobile: startActivity', {'intent': 'com.android.contacts/.activities.PeopleActivity','wait': True})
        driver.activate_app("com.google.android.contacts")
        time.sleep(3)
        # Возвращаемся в тестируемое приложение
        driver.activate_app(current_package)
        
        # Проверяем главный экран
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "sec-floors"))).is_displayed()




@pytest.mark.network

class TestCommon:

    def test_demostand_autorisation_right(self, driver):
        """Тест проводит попытку авторизации на демо-стенде с верными данными"""
        if not check_network_connection:
            pytest.skip("Пропуск: отсутствует интернет-соединение")
        try:
            favorites_button = driver.find_element(*AndroidLocators.FAVORITES_BUTTON)
            favorites_button.click()
            home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
            settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
            settings_button.click()
            connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
            connection_button.click()
            # driver.back()
            time.sleep(1)
            key_field = driver.find_element(*AndroidLocators.KEY_FILED)
            key_field.clear()
            key_field.send_keys("1212121212121212")
            home_button.click()
            time.sleep(10)
            take_screenshot(driver,"stand_auto")
            # проверки после клика
            assert "Гостиная" in driver.page_source, "Не прошла авторизация на демо-стенде"
            
        except Exception as e:
            take_screenshot(driver, "ошибка авторизации")
            pytest.fail(f"ошибка авторизации: {str(e)}")
    
    def test_local_autorisation_right(self, driver):
        """Тест проводит попытку авторизации на демо-стенде с верными данными"""
        if not check_network_connection:
            pytest.skip("Пропуск: отсутствует интернет-соединение")
        try:
            favorites_button = driver.find_element(*AndroidLocators.FAVORITES_BUTTON)
            favorites_button.click()
            home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
            settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
            settings_button.click()
            connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
            connection_button.click()
            time.sleep(1)
            key_field = driver.find_element(*AndroidLocators.KEY_FILED)
            key_field.clear()
            key_field.send_keys("1234567890123456")
            home_button.click()
            time.sleep(10)
            take_screenshot(driver,"local_stand_auto")
            # проверки после клика - есть ли карточка "Setup" в page_source
            assert "Setup" in driver.page_source, "Не прошла авторизация на демо-стенде"
            
        except Exception as e:
            take_screenshot(driver, "ошибка авторизации")
            pytest.fail(f"ошибка авторизации: {str(e)}")

    def test_demostand_autorisation_wrong(self, driver):
        """Тест проводит попытку авторизации на демо-стенде с неверными данными"""
        if not check_network_connection:
            pytest.skip("Пропуск: отсутствует интернет-соединение")
        try:
            favorites_button = driver.find_element(*AndroidLocators.FAVORITES_BUTTON)
            favorites_button.click()
            home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
            settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
            settings_button.click()
            connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
            connection_button.click()
            # driver.back()
            time.sleep(1)
            key_field = driver.find_element(*AndroidLocators.KEY_FILED)
            key_field.clear()
            key_field.send_keys("121212145454212121214")
            home_button.click()
            time.sleep(10)
            take_screenshot(driver,"stand_auto")
            # проверки после клика
            assert "Гостиная" not in driver.page_source, "Прошла авторизация с неправильными данными"
            
        except Exception as e:
            take_screenshot(driver, "авторизация с неверными данными")
            pytest.fail(f"авторизация с неверными данными: {str(e)}")

# 3. Управление устройствами
class TestDeviceControl:
    def test_main_screen_ui(self, driver):
        """Проверка главного экрана"""
        # Проверяем таб-бар

        # Проверяем зоны демо-стенда

    
   



    def test_dimmer_control(self, driver):
        """Тест управления диммером"""
        living_room = driver.find_element(*AndroidLocators.LIVING_ROOM)
        living_room.click()
        
        dimmer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "dimmer_control")))
        
        # Проверяем начальное состояние
        assert "gray" in dimmer.get_attribute("color")
        
        # Включаем
        dimmer.click()
        assert "blue" in dimmer.get_attribute("color")
        
        # Проверяем ползунок
        slider = driver.find_element(AppiumBy.ID, "brightness_slider")
        driver.swipe(slider.location['x'], slider.location['y'], 
                    slider.location['x'] + 200, slider.location['y'], 500)
        
    def test_rgb_control(self, driver):
        """Тест RGB-устройств"""
        living_room = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                        'new UiSelector().textContains("ГОСТИНАЯ")')
        living_room.click()
        
        rgb_device = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "rgb_control")))
        rgb_device.click()
        
        # Выбираем цвет
        color_picker = driver.find_element(AppiumBy.ID, "color_picker")
        color_picker.click()
        
        red = driver.find_element(AppiumBy.ID, "red_color")
        red.click()
        
        assert "red" in rgb_device.get_attribute("color")









@pytest.mark.tech
def test_1(driver):
    element = driver.find_element(*AndroidLocators.CONNECTION_TYPE)
    element.click()
    conn_type = (driver.find_element(*AndroidLocators.CONNECTION_TYPE_HOME))
    conn_type.click()
    time.sleep(2)
    # driver.back()

    assert True , "проверочный тест"



        #     def test_demostand(self, driver):
        #     assert

        # def test_demostand(self, driver):
        #     assert

        # def test_demostand(self, driver):
        #     assert