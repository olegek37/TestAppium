import pytest
import requests
import random
from tests.common.helpers import *
from tests.common.locators import IOSLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from appium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput






# первая попытка

# def test_home_content(driver):

#     # menu_items = ["Дом", "Избранные", "Оповещения", "Настройки"]
#     # for item in menu_items:
#     #     assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, item).is_displayed()
    
#     # element = driver.find_elements(AppiumBy.CLASS_NAME, 'XCUIElementTypeLink')  находит 4 кнопки меню
#     # element = driver.find_elements(AppiumBy.CLASS_NAME, 'XCUIElementTypeOther')
#     # element = driver.find_elements(AppiumBy.CLASS_NAME, 'XCUIElementTypeOther')
#     # for i in range(len(element)):
#     #     print(f"Enabled: {element[i].get_attribute('enabled')}")
#     #     print(f"Visible: {element[i].get_attribute('visible')}") 
#     #     print(f"Name: {element[i].get_attribute('name')}")
#     #     print(f"Value: {element[i].get_attribute('value')}")
#     #     print ('------------------------------')
#     #     time.sleep(1)
#     # while True: 
#     #     for i in range(len(element)):
#     #         WebDriverWait(driver, 3).until(EC.element_to_be_clickable(element[i])).click()
#     #         time.sleep(2)
#     # while True:
#     #     path = "other"
#     #     os.makedirs(path, exist_ok=True)
#     #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     #     page_source = driver.page_source
#     #     filename = os.path.join(path, f"ps_{timestamp}.xml")
#     #     with open(filename, "w", encoding="utf-8") as file:
#     #         file.write(page_source)
#     #     print(page_source )
#     #     time.sleep(4)

#     assert True



# # вторая попытка

# # Создаем папку и общий файл
#     path = "other"
#     os.makedirs(path, exist_ok=True)
#     common_file = os.path.join(path, "all_windows.xml")

#     # Храним хэши предыдущих страниц для избежания дубликатов
#     previous_hashes = set()

#     with open(common_file, "w", encoding="utf-8") as output_file:
#         output_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<all_windows>\n")
        
#         while True:
#             try:
#                 # Получаем текущую страницу
#                 page_source = driver.page_source
#                 current_hash = hash(page_source)
                
#                 # Проверяем, не была ли уже эта страница записана
#                 if current_hash not in previous_hashes:
#                     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
#                     # Добавляем в общий файл с меткой времени
#                     output_file.write(f"\n<window timestamp=\"{timestamp}\">\n")
#                     output_file.write(page_source)
#                     output_file.write("\n</window>\n")
#                     output_file.flush()  # Принудительно записываем в файл
                    
#                     # Сохраняем хэш для проверки дубликатов
#                     previous_hashes.add(current_hash)
#                     print(f"Добавлено новое окно: {timestamp}")
                
#                 time.sleep(4)
                
#             except KeyboardInterrupt:
#                 print("\nПрерывание пользователем")
#                 break

#         # Закрываем XML структуру
#         output_file.write("</all_windows>")

#     print(f"Все данные сохранены в: {common_file}")
#     assert True





# def test_find_clickable_elements(driver, sleep_time=3):
#     """Простой поиск кликабельных элементов в бесконечном цикле"""
    
#     while True:
#         print("\n" + "="*50)
#         print("ПОИСК КЛИКАБЕЛЬНЫХ ЭЛЕМЕНТОВ:")
#         print("="*50)
        
#         # Все возможные кликабельные классы iOS
#         classes = ['XCUIElementTypeButton', 'XCUIElementTypeLink', 
#                   'XCUIElementTypeCell', 'XCUIElementTypeStaticText', 
#                   'XCUIElementTypeOther']
        
#         for class_name in classes:
#             try:
#                 elements = driver.find_elements(AppiumBy.CLASS_NAME, class_name)
#                 for i, element in enumerate(elements):
#                     try:
#                         if (element.is_displayed() and 
#                             element.get_attribute('name') !='None' and
#                             element.get_attribute('enabled') == 'true' and
#                             element.size['width'] > 20 and 
#                             element.size['height'] > 20):
                            
#                             name = element.get_attribute('name')
#                             value = element.get_attribute('value')
                            
#                             print(f"\n🎯 {class_name}:")
#                             print(f"   Name: '{name}'")
#                             print(f"   Value: '{value}'")
#                             print(f"   Size: {element.size['width']}x{element.size['height']}")
#                             if name != 'N/A':
#                                 print(f"   Локатор: driver.find_element(By.NAME, '{name}')")
                            
#                     except:
#                         continue
#             except:
#                 continue
        
#         print(f"\n⏳ Жду {sleep_time} сек...")
#         time.sleep(sleep_time)



# def test_simple_find_and_click(driver, sleep_time=3):
#     """Упрощенный поиск и клик без использования current_url"""
    
#     try:
#         # Ищем любые кликабельные элементы
#         elements = driver.find_elements(AppiumBy.CLASS_NAME, 'XCUIElementTypeButton')
#         elements.extend(driver.find_elements(AppiumBy.CLASS_NAME, 'XCUIElementTypeLink'))
        
#         for element in elements:
#             try:
#                 if (element.is_displayed() and 
#                     element.get_attribute('enabled') == 'true' and
#                     element.get_attribute('name')):
                    
#                     name = element.get_attribute('name')
#                     print(f"🖱️ Кликаем на: {name}")
                    
#                     element.click()
#                     time.sleep(3)  # Ждем перехода
                    
#                     print("✅ Клик выполнен успешно")
                    
#                     # Возвращаемся назад после клика
#                     try:
#                         driver.back()
#                         time.sleep(2)
#                         print("🔙 Успешно вернулись назад")
#                     except Exception as e:
#                         print(f"❌ Ошибка при возврате: {e}")
                    
#                     return True
                    
#             except Exception as e:
#                 continue
                
#     except Exception as e:
#         print(f"❌ Ошибка при поиске элементов: {e}")
    
#     print("❌ Не удалось найти кликабельный элемент")
#     return False


# def test_find_and_click_all_elements(driver, sleep_time=3):
#     """Поиск и клик по ВСЕМ найденным элементам по очереди"""
    
#     print("🚀 Запуск поиска и клика по всем элементам...")
#     print("🛑 Для остановки нажмите Ctrl+C")
    
#     cycle_count = 0
    
#     while True:
#         cycle_count += 1
#         print(f"\n" + "="*60)
#         print(f"🔍 ЦИКЛ {cycle_count}: ПОИСК ЭЛЕМЕНТОВ")
#         print("="*60)
        
#         # Все возможные кликабельные классы
#         classes = ['XCUIElementTypeButton', 'XCUIElementTypeLink', 
#                   'XCUIElementTypeCell', 'XCUIElementTypeStaticText',
#                   'XCUIElementTypeOther']
        
#         found_elements = []
        
#         # Собираем все подходящие элементы
#         for class_name in classes:
#             try:
#                 elements = driver.find_elements(AppiumBy.CLASS_NAME, class_name)
                
#                 for element in elements:
#                     try:
#                         if (element.is_displayed() and 
#                             element.get_attribute('enabled') == 'true' and
#                             element.get_attribute('name')):
                            
#                             name = element.get_attribute('name')
#                             value = element.get_attribute('value') or 'N/A'
#                             element_type = class_name.replace('XCUIElementType', '')
                            
#                             found_elements.append({
#                                 'element': element,
#                                 'name': name,
#                                 'value': value,
#                                 'type': element_type,
#                                 'class': class_name
#                             })
                            
#                     except Exception:
#                         continue
                        
#             except Exception:
#                 continue
        
#         # Обрабатываем все найденные элементы
#         if found_elements:
#             print(f"✅ Найдено {len(found_elements)} элементов:")
            
#             for i, item in enumerate(found_elements, 1):
#                 print(f"{i}. {item['type']}: '{item['name']}'")
            
#             print(f"\n🖱️ Пытаемся кликнуть на все элементы по очереди:")
            
#             # Проходим по всем элементам и пытаемся кликнуть
#             for i, item in enumerate(found_elements, 1):
#                 try:
#                     print(f"\n{i}. Кликаем на: '{item['name']}'")
#                     print(f"   Тип: {item['type']}")
#                     print(f"   Value: '{item['value']}'")
                    
#                     # ГОТОВЫЕ ЛОКАТОРЫ
#                     print(f"   🎯 ЛОКАТОРЫ:")
#                     print(f"      • By.NAME: driver.find_element(AppiumBy.NAME, '{item['name']}')")
#                     print(f"      • Accessibility ID: driver.find_element(AppiumBy.ACCESSIBILITY_ID, '{item['name']}')")
#                     print(f"      • XPATH: driver.find_element(AppiumBy.XPATH, \"//{item['class']}[@name='{item['name']}')")
                    
#                     # Пытаемся кликнуть
#                     item['element'].click()
#                     print(f"   ✅ КЛИК УСПЕШЕН!")
                    
#                     # Ждем немного
                    
                    
#                     # Возвращаемся назад
#                     print("   ⏳ Ожидаю ручного клика назад...")
#                     print("   🖱️ Кликните кнопку назад в приложении")
#                     time.sleep(2)  # Даем 3 секунды на ручной клик
                    
#                 except Exception as e:
#                     print(f"   ❌ Ошибка клика: {e}")
#                     continue
                    
#             print(f"\n✅ ЗАВЕРШЕНО: обработано {len(found_elements)} элементов")
            
#         else:
#             print("❌ Элементы не найдены")
        
#         print(f"\n⏳ Следующий цикл через {sleep_time} сек...")
#         time.sleep(sleep_time)


def test_1(driver):
    # element = driver.find_element(*IOSLocators.CONNECTION_BUTTON)
    element = driver.find_element(*IOSLocators.HOME_BUTTON)
    element.click()
    # time.sleep(2)
    # element = driver.find_element(*IOSLocators.CONNECTION_BUTTON)
    # element.click()
    # driver.back()

    assert True , "проверочный тест"


def test_app_launch_and_restart(driver):
    """Тест запуска и перезапуска приложения"""
    driver.find_element(*IOSLocators.HOME_BUTTON).click()
    # Проверяем, что приложение запустилось
    assert "Setup" in driver.page_source
    
    # Сворачиваем приложение
    driver.background_app(-1)
    
    # Разворачиваем приложение обратно
    driver.launch_app()
    
    # Проверяем, что приложение восстановилось
    assert "Setup" in driver.page_source




def test_local_autorisation_right(driver):
    """Тест проводит попытку авторизации на демо-стенде с верными данными"""
    # if not check_network_connection:
    #     pytest.skip("Пропуск: отсутствует интернет-соединение")
    try:
        favorites_button = driver.find_element(*IOSLocators.FAVORITES_BUTTON)
        favorites_button.click()
        settings_button = driver.find_element(*IOSLocators.SETTINGS_BUTTON)
        settings_button.click()
        connection_button = driver.find_element(*IOSLocators.CONNECTION_BUTTON)
        connection_button.click()
        time.sleep(1)
        key_field = driver.find_element(*IOSLocators.KEY_FILED)
        key_field.clear()
        key_field.send_keys("1234567890123456")
        connect_text = driver.find_element(*IOSLocators.CONNECT_TEXT)
        connect_text.click()
        time.sleep(2)
        home_button = driver.find_element(*IOSLocators.HOME_BUTTON)
        home_button.click()
        time.sleep(10)
        take_screenshot(driver,"local_stand_auto")
        # проверки после клика - есть ли карточка "Setup" в page_source
        assert "Setup" in driver.page_source, "Не прошла авторизация на демо-стенде"
    except Exception as e:
        take_screenshot(driver, "ошибка авторизации")
        pytest.fail(f"ошибка авторизации: {str(e)}")


# def test_change_widget_image(driver):
   
#     try:
#         # 1. Длительное нажатие на виджет
#         widget_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Гостиная")
#         action = webdriver.common.touch_action.TouchAction(driver)
#         action.long_press(widget_element, duration=2000).perform()
        
#         # 2. Ждем появления контейнера с картинками
#         time.sleep(2)  # можно заменить на явное ожидание
        
#         # 3. Находим все контейнеры с картинками
#         containers = driver.find_elements(
#             AppiumBy.XPATH, 
#             "//XCUIElementTypeOther"
#         )
        
#         # 4. Определяем текущий выбранный элемент
#         selected_container = None
#         for container in containers:
#             try:
#                 # Ищем изображение галочки
#                 container.find_element(AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
#                 selected_container = container
#                 break
#             except:
#                 continue
        
#         # 5. Выбираем другой элемент
#         target_container = None
#         for container in containers:
#             if container != selected_container:
#                 try:
#                     # Проверяем отсутствие галочки
#                     container.find_element(AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
#                 except:
#                     target_container = container
#                     break
        
#         # 6. Кликаем по выбранному элементу
#         if target_container:
#             target_container.click()
#             time.sleep(1)  # ждем применения изменений
            
#             # Проверяем, что галочка переместилась
#             new_selected = driver.find_elements(
#                 AppiumBy.XPATH, 
#                 "//XCUIElementTypeOther[contains(.//XCUIElementTypeImage)]"
#             )
            
#             assert target_container in new_selected, "Картинка не была успешно изменена"
#         else:
#             assert False, "Не удалось найти альтернативный элемент для выбора"
            
#     finally:
#         driver.quit()

#4 Долгое удержание карточки зоны - выбор картинки из медиатеки
def test_zone_image_change(driver):
    """Изменение картинки зоны"""
    driver.find_element(*IOSLocators.HOME_BUTTON).click()


    # Находим карточку зоны
    zone_card = driver.find_element(*IOSLocators.ZONE_LOCAL)
    
    # Долгое нажатие
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(
        zone_card.location['x'] + zone_card.size['width'] / 2,
        zone_card.location['y'] + zone_card.size['height'] / 2
    )
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(2)
    actions.w3c_actions.pointer_action.pointer_up()
    actions.w3c_actions.perform()
    
    # Выбор картинки из медиатеки
    driver.find_element(*IOSLocators.PHONE_GALLERY).click()


    # Выбор конкретного изображения
    images_layout = driver.find_element(*IOSLocators.PHONE_GALLERY_LAYOUT)
    print (images_layout)
    images = images_layout.find_elements(AppiumBy.CLASS_NAME,"XCUIElementTypeImage" )
    images[2].click()  # Выбираем четвертое изображение
    
    # Проверка уведомления
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(IOSLocators.PHOTO_CH_NOTIFY)
    ).is_displayed()




#5 Клик по иконке - включение виджетов

def test_element_state_changes_after_click(driver):
    """Проверяет, что статус элемента изменяется после клика в UI.""" 
    target_element_id = "788:3"
    driver.find_element(*IOSLocators.MENU_LIGHTING).click()
    try:
        #  Получаем исходное состояние элемента через API---
        auth_token =  get_token()
        initial_state = get_element_state(auth_token,target_element_id )

        print(f"Исходное состояние элемента {target_element_id}: {initial_state}")
        
        #  Кликаем на элемент в лампа---
        
        ui_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(IOSLocators.LAMP_3))
        ui_element.click()
        print("Клик выполнен успешно.")
        
        #Получаем новое состояние 
        time.sleep(1)  
        new_state = get_element_state(auth_token,target_element_id )
        print(f"Новое состояние элемента {target_element_id}: {new_state}")

        driver.find_element(*IOSLocators.HOME_BUTTON).click()
        
        # Assert - Проверяем, что состояние изменилось ---
        assert new_state != initial_state, (
            f"Состояние элемента {target_element_id} не изменилось после клика. "
            f"Было: '{initial_state}', стало: '{new_state}'."
        )
        
            
    except Exception as e:
        pytest.fail(f"Тест завершился с ошибкой: {e}")

#6 Долгое удержание иконки - откывается модальное окно

def test_long_press_modal(driver):
    """Долгое удержание для открытия модального окна"""
    driver.find_element(*IOSLocators.MENU_LIGHTING).click()

    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(IOSLocators.LAMP_3))

    # Долгое нажатие
    actions = ActionChains(driver)
    actions.w3c_actions.pointer_action.move_to_location(
    element.location['x'] + element.size['width'] / 2,
    element.location['y'] + element.size['height'] / 2
    )
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(2)
    actions.w3c_actions.pointer_action.pointer_up()
    actions.w3c_actions.perform()


    # Проверка элементов модального окна
    elements_to_check = [
        '//XCUIElementTypeStaticText[@name="Управление"]',
        '//XCUIElementTypeStaticText[@name="Статистика"]',
        '//XCUIElementTypeStaticText[@name="Оповещения"]'
    ]
    
    for xpath in elements_to_check:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
        )
        assert element.is_displayed()

def test_group_actions(driver):
    """Проверка групповых действий Вкл всё/Выкл всё"""
    driver.find_element(*IOSLocators.MENU_LIGHTING).click()
    auth_token = get_token()
    
    # ID всех ламп от 788:1 до 788:8
    lamp_ids = [f"788:{i}" for i in range(1, 9)]
    
    # Получаем начальные состояния всех ламп
    initial_states = {}
    for lamp_id in lamp_ids:
        initial_states[lamp_id] = get_element_state(auth_token, lamp_id)
    
    # Кликаем "Включить все"
    driver.find_element(*IOSLocators.ALL_ON).click()
    time.sleep(2)
    
    # Проверяем, что все лампы включились (статус "01")
    for lamp_id in lamp_ids:
        new_state = get_element_state(auth_token, lamp_id)
        assert new_state == "01", f"Лампа {lamp_id} не включилась. Состояние: {new_state}"
    
    # Кликаем "Выключить все" 
    driver.find_element(*IOSLocators.ALL_OFF).click()
    time.sleep(2)
    
    # Проверяем, что все лампы выключились (статус "00")
    for lamp_id in lamp_ids:
        new_state = get_element_state(auth_token, lamp_id)
        assert new_state == "00", f"Лампа {lamp_id} не выключилась. Состояние: {new_state}"
    
    driver.find_element(*IOSLocators.HOME_BUTTON).click()

def test_bottom_menu(driver):
    """Проверка навигации по меню с проверками"""
    for _ in range(10):
        # Нижнее меню
        for btn in [IOSLocators.HOME_BUTTON, IOSLocators.SETTINGS_BUTTON, 
                   IOSLocators.FAVORITES_BUTTON, IOSLocators.NOTICE_BUTTON]:
            driver.find_element(*btn).click()
            assert driver.page_source != ""  # Не пустой экран
        
        # Настройки
        driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
        assert "Настройки" in driver.page_source
        
        # Пункты настроек
        for setting in [IOSLocators.COMMON_BUTTON, IOSLocators.CONNECTION_BUTTON,
                       IOSLocators.NOTIFY_BUTTON, IOSLocators.ABOUT_BUTTON]:
            driver.find_element(*setting).click()
            assert driver.page_source != ""  # Страница загрузилась
            driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
            assert "Настройки" in driver.page_source  # Вернулись в настройки
        
        # Оповещения и возврат
        driver.find_element(*IOSLocators.NOTICE_BUTTON).click()
        assert "Оповещения" in driver.page_source
        driver.find_element(*IOSLocators.SETTINGS_BUTTON).click()
        assert "Настройки" in driver.page_source
        driver.find_element(*IOSLocators.HOME_BUTTON).click()
        assert "Setup" in driver.page_source

def test_categories_menu(driver):
    """Проверка меню категорий """
    driver.find_element(*IOSLocators.HOME_BUTTON).click()
    assert driver.page_source != ""
    
    # Основные категории
    for cat in [IOSLocators.MENU_SCENARIOS, IOSLocators.MENU_LIGHTING,
               IOSLocators.MENU_CURTAINS, IOSLocators.MENU_CLIMATE,
               IOSLocators.MENU_SECURITY]:
        driver.find_element(*cat).click()
        assert driver.page_source != ""
    
    # Свайп влево для открытия бокового меню
    elem = driver.find_element(*IOSLocators.MENU_SECURITY)
    driver.swipe(elem.location['x'] + 150, elem.location['y'] + 50, 
                elem.location['x'] - 150, elem.location['y'] + 50, 800)
    
    # Боковое меню
    for item in [IOSLocators.MENU_SENSORS, IOSLocators.MENU_OTHER, IOSLocators.MENU_MUSIC]:
        driver.find_element(*item).click()
        assert driver.page_source != ""

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
