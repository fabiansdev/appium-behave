import os

PACKAGE = 'com.disney.wdpro.dlr'
APPIUM_URL = 'http://127.0.0.1:4723/wd/hub'
APK_NAME = 'disney.apk'
APK_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), APK_NAME))

DESIRED_CAPABILITIES = {
    'app': APK_PATH,
    'appPackage': PACKAGE,
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': 'Nexus_5X_Disney_App',
    "appActivity": 'com.disney.wdpro.park.activities.LoaderActivity',
}
