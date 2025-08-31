import base64
import os
import json
import requests
from datetime import datetime
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver, test_name, path="screenshots"):
    """Функция для создания скриншотов"""
    try:
        os.makedirs(path, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(path, f"{test_name}_{timestamp}.png")
        
        screenshot = driver.get_screenshot_as_base64()
        with open(filename, "wb") as f:
            f.write(base64.b64decode(screenshot))
        
        print(f"Screenshot saved: {filename}")
        return filename
    except Exception as e:
        print(f"Screenshot error: {e}")
        return None
    
    
def check_network_connection(driver: webdriver) -> bool:
    """Проверяем доступность интернета на телефоне"""
    try:
        output = driver.execute_script('mobile: shell', {
            'command': 'ping',
            'args': ['-c', '1', '8.8.8.8']
        })
        return "1 received" in output
    except:
        return False
    


# def select_connection_type(connection_type_locator):
#     try:
#         element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(connection_type_locator)
#     except Exception as e:
#         print(f"Screenshot error: {e}")
#         return None


# async def get_element_state_via_ws(target_element_id):
#     """Асинхронная функция для получения состояния элемента через WebSocket."""
#     async with websockets.connect('ws://192.168.1.125:55550') as ws:
#         # Аутентификация
#         await ws.send(json.dumps({
#             "command": "get_token",
#             "username": "mimismart", 
#             "password": "1234567890123456"
#         }))
#         token_msg = await ws.recv()
#         token_data = json.loads(token_msg)
#         token = token_data['access_token']
        
#         await ws.send(json.dumps({
#             "command": "auth", 
#             "access_token": token
#         }))
#         auth_msg = await ws.recv()
#         print(f"🔑 Auth response: {auth_msg}")
        
#         # Получаем все items (состояния)
#         await ws.send(json.dumps({"command": "get_items"}))
#         items_msg = await ws.recv()
#         items_data = json.loads(items_msg)
        
#         # Ищем нужный элемент в данных
#         # Структура ответа может быть разной, предположим, что состояния в items_data['data']
#         if 'data' in items_data and target_element_id in items_data['data']:
#             return items_data['data'][target_element_id]
#         else:
#             return None
        

def get_token():
    """Получает токен авторизации"""
    response = requests.post(
        'http://192.168.1.125:55550/token/',
        data='grant_type=password&username=mimismart&password=1234567890123456&scope=&client_id=string&client_secret=string',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    return response.json()['access_token']


def get_element_state(token, element_id):
    """Получает состояние элемента по ID"""
    response = requests.get(
        'http://192.168.1.125:55550/item/get_all_states/',
        headers={'Authorization': f'Bearer {token}'}
    )
    return response.json()['data'][element_id]