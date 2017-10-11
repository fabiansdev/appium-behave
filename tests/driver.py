from appium import webdriver
from settings import APPIUM_URL, DESIRED_CAPABILITIES

class Driver(object):

    package = DESIRED_CAPABILITIES['appPackage']
    driver = webdriver.Remote(command_executor=APPIUM_URL,
        desired_capabilities=DESIRED_CAPABILITIES
    )

    def close(self):
        self.driver.quit()
