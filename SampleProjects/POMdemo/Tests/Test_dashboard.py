import unittest
import time
from selenium import webdriver
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
from HTMLTestRunner import HTMLTestRunner


# add global delay for each test without adding time.sleep
def add_delay(delay_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(delay_time)  # Delay before the method
            result = func(*args, **kwargs)
            time.sleep(delay_time)  # Delay after the method
            return result

        return wrapper

    return decorator


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.delay_time = 2  # Set a global delay time in seconds

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("kk116402", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(self.delay_time)  # Global delay before each test

    def tearDown(self):
        time.sleep(self.delay_time)  # Global delay after each test
        self.driver.quit()

    @add_delay(2)
    def test_click_schedule_link(self):
        self.dashboard_page.click_schedule_link()
        # Add assertions or further steps after clicking schedule link

    @add_delay(2)
    def test_click_leave_request_link(self):
        time.sleep(2)
        self.dashboard_page.click_leave_request_link()
        time.sleep(2)
        # Add assertions or further steps after clicking leave request link

    @add_delay(2)
    def test_click_availability_link(self):
        self.dashboard_page.click_availability_link()
        # Add assertions or further steps after clicking availability link

    @add_delay(2)
    def test_click_notification_link(self):
        self.dashboard_page.click_notification_link()
        # Add assertions or further steps after clicking notification link

    @add_delay(2)
    def test_click_bid_link(self):
        self.dashboard_page.click_Bid_link()
        # Add assertions or further steps after clicking bid link

    @add_delay(2)
    def test_click_Punch_link(self):
        self.dashboard_page.click_Punch_link()
        # Add assertions or further steps after clicking bid link


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='reports'))
