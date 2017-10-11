from behave import *
from activities.base import BaseActivity
import time

@given('I click on the Disney button')
def step_impl(context):
    time.sleep(5)
    BaseActivity.swipe(500, 100, 500, 800, 300)
    time.sleep(5)
    button_one = BaseActivity.find_by_id(BaseActivity.disney_img_id)
    button_one.click()
