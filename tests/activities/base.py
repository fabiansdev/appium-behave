from driver import Driver

class BaseActivity():

    #locators
    disney_img_id = ":id/img_avatar"

    def find_by_id(name):
        element = Driver.driver.find_element_by_id(Driver.package + name)
        return element

    def swipe(x1, y1, x2, y2, time):
        Driver.driver.swipe(x1, y1, x2, y2, time)
