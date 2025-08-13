import base64
import os
from datetime import datetime

def take_screenshot(driver, test_name, path="screenshots"):
    """Универсальная функция для создания скриншотов"""
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