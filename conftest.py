import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import os

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android", help="platform to test: android or ios")
    parser.addoption("--appium_server", action="store", default="http://192.168.1.253:4723", help="Appium server URL")

@pytest.fixture(scope='session')
def appium_server(request):
    return request.config.getoption("--appium_server")
 
@pytest.fixture(scope='function')
def driver(request, appium_server):
    platform = request.config.getoption("--platform")
    
    if platform == "android":
        capabilities = {
            "platformName": "Android",
            "appium:platformVersion": "15",
            "appium:deviceName": "Pixel 9 Pro API 35",
            "appium:automationName": "UiAutomator2",
            "appium:app": "/Users/lehu4ka/app/mimi.apk",
            "appium:noReset": True
        }
        options = UiAutomator2Options().load_capabilities(capabilities)
    else:  # iOS
        capabilities = {
            "platformName": "iOS",
            "appium:platformVersion": "18.2",
            "appium:deviceName": "iPhone 16 Pro",
            "appium:automationName": "XCUITest",
            "appium:bundleId": "com.mimismart.app",
            "appium:noReset": True,
            "appium:autoAcceptAlerts": True  # автоматически принимать системные алерты
        }
        options = XCUITestOptions().load_capabilities(capabilities)
    
    driver = webdriver.Remote(command_executor=appium_server, options=options)

    yield driver
    
    driver.quit()
