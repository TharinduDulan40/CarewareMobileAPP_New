import unittest
from selenium import webdriver
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
from HTMLTestRunner import HTMLTestRunner


class TestDashboardPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("bskaria", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_click_schedule_link(self):
        self.dashboard_page.click_schedule_link()
        # Add assertions or further steps after clicking schedule link

    def test_click_leave_request_link(self):
        self.dashboard_page.click_leave_request_link()
        # Add assertions or further steps after clicking leave request link

    def test_click_availability_link(self):
        self.dashboard_page.click_availability_link()
        # Add assertions or further steps after clicking availability link

    def test_click_notification_link(self):
        self.test_click_notification_link()
    # Add other test methods for the dashboard page as needed


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='reports'))
