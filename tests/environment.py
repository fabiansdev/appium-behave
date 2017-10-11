import os
from appium import webdriver
from driver import Driver

def before_all(context):
    context.driver = Driver()

def after_all(context):
    context.driver.close()
