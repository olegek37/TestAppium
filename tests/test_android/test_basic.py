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
import time
import random



    
def test_local_autorisation_right(driver):
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


def test_cold_start(driver):
    """Проверка холодного старта приложения"""
    main_screen = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((AppiumBy.ID, "sec-floors")))
    assert main_screen.is_displayed(), "Главный экран не отображается после холодного старта"
    
def test_hot_start(driver):
    """Проверка горячего старта приложения"""
    driver.background_app(-1)
    main_screen = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "sec-floors")))
    assert main_screen.is_displayed(), "Главный экран не отображается после горячего старта"


def test_app_launch_and_restart(driver):
    """Тест запуска и перезапуска приложения"""
    driver.find_element(*AndroidLocators.HOME_BUTTON).click()
    assert "Setup" in driver.page_source
    
    # Для Android: background_app может работать иначе
    driver.background_app(-1)
    driver.launch_app()
    assert "Setup" in driver.page_source

def test_interruptions(driver):
    
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



def test_zone_image_change(driver):
    """Изменение картинки зоны"""
    driver.find_element(*AndroidLocators.HOME_BUTTON).click()
    zone_card = driver.find_element(*AndroidLocators.ZONE_LOCAL)
    
    # Долгое нажатие для Android - МОБИЛЬНАЯ КОМАНДА МОЖЕТ ОТЛИЧАТЬСЯ!
    # Для Android обычно используется touchAction или alternative метод
    try:
        # Попробуем стандартный способ
        driver.execute_script("mobile: longClickGesture", {
            "elementId": zone_card.id,
            "duration": 2000
        })
    except:
        # Альтернатива для Android
        from appium.webdriver.common.touch_action import TouchAction
        action = TouchAction(driver)
        action.long_press(zone_card, duration=2000).release().perform()
    
    driver.find_element(*AndroidLocators.PHONE_GALLERY).click()
    
    # Выбор изображения - класс для Android другой
    images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
    if len(images) >= 3:
        images[2].click()
    
    assert WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(AndroidLocators.PHOTO_CH_NOTIFY)
    )

def test_element_state_changes_after_click(driver):
    """Изменение статуса элемента после клика"""
    # Этот тест полностью аналогичен iOS, так как использует только базовые методы
    target_element_id = "788:3"
    driver.find_element(*AndroidLocators.MENU_LIGHTING).click()
    
    auth_token = get_token()
    initial_state = get_element_state(auth_token, target_element_id)
    
    ui_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AndroidLocators.LAMP_3)
    )
    ui_element.click()
    
    time.sleep(1)
    new_state = get_element_state(auth_token, target_element_id)
    
    driver.find_element(*AndroidLocators.HOME_BUTTON).click()
    assert new_state != initial_state

def test_long_press_modal(driver):
    """Открытие модального окна долгим нажатием"""
    driver.find_element(*AndroidLocators.MENU_LIGHTING).click()
    
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AndroidLocators.LAMP_3)
    )
    
    # Долгое нажатие с обработкой возможных отличий
    try:
        driver.execute_script("mobile: longClickGesture", {
            "elementId": element.id,
            "duration": 2000
        })
    except:
        from appium.webdriver.common.touch_action import TouchAction
        action = TouchAction(driver)
        action.long_press(element, duration=2000).release().perform()
    
    # Проверка элементов модального окна для Android
    elements_xpath = [
        '//android.widget.TextView[@text="Управление"]',
        '//android.widget.TextView[@text="Статистика"]', 
        '//android.widget.TextView[@text="Оповещения"]'
    ]
    
    for xpath in elements_xpath:
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
        )

def test_group_actions(driver):
    """Групповые действия Вкл всё/Выкл всё"""
    # Аналогично iOS - только базовые методы
    driver.find_element(*AndroidLocators.MENU_LIGHTING).click()
    auth_token = get_token()
    lamp_ids = [f"788:{i}" for i in range(1, 9)]
    
    driver.find_element(*AndroidLocators.ALL_ON).click()
    time.sleep(2)
    for lamp_id in lamp_ids:
        assert get_element_state(auth_token, lamp_id) == "01"
    
    driver.find_element(*AndroidLocators.ALL_OFF).click()
    time.sleep(2)
    for lamp_id in lamp_ids:
        assert get_element_state(auth_token, lamp_id) == "00"
    
    driver.find_element(*AndroidLocators.HOME_BUTTON).click()

def test_bottom_menu(driver):
    """Проверка навигации по нижнему меню"""
    # Аналогично iOS - базовые методы
    for _ in range(10):
        for btn in [AndroidLocators.HOME_BUTTON, AndroidLocators.SETTINGS_BUTTON, 
                   AndroidLocators.FAVORITES_BUTTON, AndroidLocators.NOTICE_BUTTON]:
            driver.find_element(*btn).click()
            assert driver.page_source != ""
        
        driver.find_element(*AndroidLocators.SETTINGS_BUTTON).click()
        assert "Настройки" in driver.page_source
        
        for setting in [AndroidLocators.COMMON_BUTTON, AndroidLocators.CONNECTION_BUTTON,
                       AndroidLocators.NOTIFY_BUTTON, AndroidLocators.ABOUT_BUTTON]:
            driver.find_element(*setting).click()
            assert driver.page_source != ""
            driver.find_element(*AndroidLocators.SETTINGS_BUTTON).click()
            assert "Настройки" in driver.page_source
        
        driver.find_element(*AndroidLocators.NOTICE_BUTTON).click()
        assert "Оповещения" in driver.page_source
        driver.find_element(*AndroidLocators.SETTINGS_BUTTON).click()
        assert "Настройки" in driver.page_source
        driver.find_element(*AndroidLocators.HOME_BUTTON).click()
        assert "Setup" in driver.page_source

def test_categories_menu(driver):
    """Проверка меню категорий"""
    driver.find_element(*AndroidLocators.HOME_BUTTON).click()
    assert driver.page_source != ""
    
    for cat in [AndroidLocators.MENU_SCENARIOS, AndroidLocators.MENU_LIGHTING,
               AndroidLocators.MENU_CURTAINS, AndroidLocators.MENU_CLIMATE,
               AndroidLocators.MENU_SECURITY]:
        driver.find_element(*cat).click()
        assert driver.page_source != ""
    
    # Свайп для Android - может работать иначе
    elem = driver.find_element(*AndroidLocators.MENU_SECURITY)
    try:
        # Стандартный swipe
        driver.swipe(elem.location['x'] + 150, elem.location['y'] + 50, 
                    elem.location['x'] - 150, elem.location['y'] + 50, 800)
    except:
        # Альтернатива через TouchAction
        from appium.webdriver.common.touch_action import TouchAction
        action = TouchAction(driver)
        action.press(x=elem.location['x'] + 150, y=elem.location['y'] + 50)\
              .move_to(x=elem.location['x'] - 150, y=elem.location['y'] + 50)\
              .release().perform()
    
    for item in [AndroidLocators.MENU_SENSORS, AndroidLocators.MENU_OTHER, AndroidLocators.MENU_MUSIC]:
        driver.find_element(*item).click()
        assert driver.page_source != ""


def test_sensor_panel_has_max_5_elements(driver):
    """
    Панель состояния (макс. 5 датчиков)
    Проверяем, что в панели датчиков отображается не более 5 элементов.
    """

    # !! Надо дописать "путь" до этой зоны от кнопки дом
    # Находим контейнер панели датчиков
    sensors_panel = driver.find_element(*AndroidLocators.SENSORS_PANEL_ID)

    # Находим ВСЕХ прямых потомков  android.view.View  этого контейнера.

    sensor_elements = sensors_panel.find_elements(by=AppiumBy.XPATH, value="./android.view.View")

    # Считаем количество найденных элементов-датчиков
    number_of_sensors = len(sensor_elements)
    print(f"\nNumber of sensor elements found in the panel: {number_of_sensors}")

    # 5. ОСНОВНАЯ ПРОВЕРКА: количество должно быть не более 5
    assert number_of_sensors <= 5, (
        f"Панель состояния содержит {number_of_sensors} датчиков, "
        f"но по ТЗ должно быть не более 5."
    )

def test_dark_theme_short(driver):
    """Темная тема + скриншоты"""
    # Настройки → Общие → Темная тема
    driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
    driver.find_element(*IOSLocators.COMMON_BUTTON).click()
    driver.find_element(*IOSLocators.THEME_NENU).click()
    driver.find_element(*IOSLocators.DARK_THEME).click()
    time.sleep(1)
    
    # Скриншоты всех разделов
    take_screenshot(driver, "dark_theme_settings")
    driver.find_element(*IOSLocators.NOTICE_BUTTON).click()
    take_screenshot(driver, "dark_theme_notice")
    driver.find_element(*IOSLocators.FAVORITES_BUTTON).click()
    take_screenshot(driver, "dark_theme_favorites")
    driver.find_element(*IOSLocators.HOME_BUTTON).click()
    take_screenshot(driver, "dark_theme_home")
    assert True 


def test_background_change(driver):
    """Смена фона + скриншоты нижнего меню"""
    # Настройки → Общие → Фон
    driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
    driver.find_element(*IOSLocators.COMMON_BUTTON).click()
    driver.find_element(*IOSLocators.BACKGROUND_BUTTON).click()
    
    # Выбираем случайное изображение
    images = driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
    if images:
        random.choice([img for img in images if img.is_displayed()]).click()
    
    # Скриншоты всех разделов нижнего меню
    for btn in [IOSLocators.HOME_BUTTON, IOSLocators.SETTINGS_BUTTON,
               IOSLocators.FAVORITES_BUTTON, IOSLocators.NOTICE_BUTTON]:
        driver.find_element(*btn).click()
        time.sleep(1)
        take_screenshot(driver, f"bg_{btn[1].lower()}")
    assert True

def test_chaotic_user_behavior(driver):
    """Хаотичное поведение пользователя с учетом ограничений видимости элементов"""
    # Списки кнопок по разделам
    home_buttons = [
        IOSLocators.ZONE_LOCAL,
        IOSLocators.MENU_SCENARIOS,
        IOSLocators.MENU_LIGHTING,
        IOSLocators.MENU_CURTAINS,
        IOSLocators.MENU_CLIMATE,
        IOSLocators.MENU_SECURITY
    ]
    
    settings_buttons = [
        IOSLocators.COMMON_BUTTON,
        IOSLocators.CONNECTION_BUTTON,
        IOSLocators.NOTIFY_BUTTON,
        IOSLocators.ABOUT_BUTTON
    ]
    
    bottom_buttons = [
        IOSLocators.HOME_BUTTON,
        IOSLocators.SETTINGS_BUTTON,
        IOSLocators.FAVORITES_BUTTON,
        IOSLocators.NOTICE_BUTTON
    ]
    
    for i in range(10):
        # Всегда начинаем с главного экрана
        driver.find_element(*IOSLocators.HOME_BUTTON).click()
        time.sleep(0.5)
        
        # Случайное действие
        action_type = random.choice(['home', 'settings', 'bottom'])
        
        if action_type == 'home':
            # Действия на главном экране
            random_button = random.choice(home_buttons)
            try:
                driver.find_element(*random_button).click()
                print(f"Клик на {random_button[1]}")
                time.sleep(1)
                assert driver.page_source != "", "Пустая страница после клика"
            except:
                print(f"Не удалось кликнуть на {random_button[1]}")
        
        elif action_type == 'settings':
            # Действия в настройках
            driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
            time.sleep(0.5)
            
            random_setting = random.choice(settings_buttons)
            try:
                driver.find_element(*random_setting).click()
                print(f"Клик на {random_setting[1]}")
                time.sleep(1)
                assert driver.page_source != "", "Пустая страница после клика"
            except:
                print(f"Не удалось кликнуть на {random_setting[1]}")
            
            # Возврат в настройки
            driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
        
        else:
            # Клики по нижним кнопкам (только HOME и SETTINGS имеют контент)
            random_bottom = random.choice([IOSLocators.HOME_BUTTON, IOSLocators.SETTINGS_BUTTON])
            driver.find_element(*random_bottom).click()
            print(f"Клик на {random_bottom[1]}")
            time.sleep(1)
            assert driver.page_source != "", "Пустая страница после клика"
        
        # Случайный свайп
        if random.choice([True, False]):
            width = driver.get_window_size()['width']
            height = driver.get_window_size()['height']
            direction = random.choice(['up', 'down', 'left', 'right'])
            
            if direction == 'up':
                driver.swipe(width/2, height*0.7, width/2, height*0.3, 300)
            elif direction == 'down':
                driver.swipe(width/2, height*0.3, width/2, height*0.7, 300)
            elif direction == 'left':
                driver.swipe(width*0.7, height/2, width*0.3, height/2, 300)
            else:
                driver.swipe(width*0.3, height/2, width*0.7, height/2, 300)
            
            print(f"Свайп {direction}")
            time.sleep(0.5)
    
    # Финальная проверка - возврат на главный экран
    driver.find_element(*IOSLocators.HOME_BUTTON).click()
    assert "Setup" in driver.page_source
    print("Тест завершен успешно")






#  --------------- Нерабочие и служебные тесты

# class TestCommon:
#     def test_demostand_autorisation_right( driver):
#         """Тест проводит попытку авторизации на демо-стенде с верными данными"""
#         if not check_network_connection:
#             pytest.skip("Пропуск: отсутствует интернет-соединение")
#         try:
#             favorites_button = driver.find_element(*AndroidLocators.FAVORITES_BUTTON)
#             favorites_button.click()
#             home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
#             settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
#             settings_button.click()
#             connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
#             connection_button.click()
#             # driver.back()
#             time.sleep(1)
#             key_field = driver.find_element(*AndroidLocators.KEY_FILED)
#             key_field.clear()
#             key_field.send_keys("1212121212121212")
#             home_button.click()
#             time.sleep(10)
#             take_screenshot(driver,"stand_auto")
#             # проверки после клика
#             assert "Гостиная" in driver.page_source, "Не прошла авторизация на демо-стенде"
            
#         except Exception as e:
#             take_screenshot(driver, "ошибка авторизации")
#             pytest.fail(f"ошибка авторизации: {str(e)}")

#     def test_demostand_autorisation_wrong(self, driver):
#         """Тест проводит попытку авторизации на демо-стенде с неверными данными"""
#         if not check_network_connection:
#             pytest.skip("Пропуск: отсутствует интернет-соединение")
#         try:
#             favorites_button = driver.find_element(*AndroidLocators.FAVORITES_BUTTON)
#             favorites_button.click()
#             home_button = driver.find_element(*AndroidLocators.HOME_BUTTON)
#             settings_button = driver.find_element(*AndroidLocators.SETTINGS_BUTTON)
#             settings_button.click()
#             connection_button = driver.find_element(*AndroidLocators.CONNECTION_BUTTON)
#             connection_button.click()
#             # driver.back()
#             time.sleep(1)
#             key_field = driver.find_element(*AndroidLocators.KEY_FILED)
#             key_field.clear()
#             key_field.send_keys("121212145454212121214")
#             home_button.click()
#             time.sleep(10)
#             take_screenshot(driver,"stand_auto")
#             # проверки после клика
#             assert "Гостиная" not in driver.page_source, "Прошла авторизация с неправильными данными"
            
#         except Exception as e:
#             take_screenshot(driver, "авторизация с неверными данными")
#             pytest.fail(f"авторизация с неверными данными: {str(e)}")

# # 3. Управление устройствами
# class TestDeviceControl:
#     def test_main_screen_ui(self, driver):
#         """Проверка главного экрана"""
#         # Проверяем таб-бар

#         # Проверяем зоны демо-стенда

#     def test_dimmer_control(self, driver):
#         """Тест управления диммером"""
#         living_room = driver.find_element(*AndroidLocators.LIVING_ROOM)
#         living_room.click()
        
#         dimmer = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((AppiumBy.ID, "dimmer_control")))
        
#         # Проверяем начальное состояние
#         assert "gray" in dimmer.get_attribute("color")
        
#         # Включаем
#         dimmer.click()
#         assert "blue" in dimmer.get_attribute("color")
        
#         # Проверяем ползунок
#         slider = driver.find_element(AppiumBy.ID, "brightness_slider")
#         driver.swipe(slider.location['x'], slider.location['y'], 
#                     slider.location['x'] + 200, slider.location['y'], 500)
        
#     def test_rgb_control(self, driver):
#         """Тест RGB-устройств"""
#         living_room = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
#                                         'new UiSelector().textContains("ГОСТИНАЯ")')
#         living_room.click()
        
#         rgb_device = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((AppiumBy.ID, "rgb_control")))
#         rgb_device.click()
        
#         # Выбираем цвет
#         color_picker = driver.find_element(AppiumBy.ID, "color_picker")
#         color_picker.click()
        
#         red = driver.find_element(AppiumBy.ID, "red_color")
#         red.click()
        
#         assert "red" in rgb_device.get_attribute("color")




    # def test_interruptions(self, driver):
    #     """Реакция на прерывания"""
    #     driver.start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        
    #     driver.start_activity("com.mimismart.app", "your.app.MainActivity")
    #     main_screen = driver.find_element(AppiumBy.ID, "sec-floors")
    #     assert main_screen.is_displayed(), "Главный экран не отображается после прерывания"


# @pytest.mark.tech
# def test_1(driver):
#     element = driver.find_element(*AndroidLocators.CONNECTION_TYPE)
#     element.click()
#     conn_type = (driver.find_element(*AndroidLocators.CONNECTION_TYPE_HOME))
#     conn_type.click()
#     time.sleep(2)
#     # driver.back()

#     assert True , "проверочный тест"

