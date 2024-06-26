import unittest
from selenium import webdriver
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException


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

    def tearDown(self):
        self.driver.quit()

    def test_click_schedule_link(self):
        try:
            self.dashboard_page.click_schedule_link()
            # Add assertions or further steps after clicking schedule link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click schedule link: {e}")

    def test_click_leave_request_link(self):
        try:
            self.dashboard_page.click_leave_request_link()
            # Add assertions or further steps after clicking leave request link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click leave request link: {e}")

    def test_click_availability_link(self):
        try:
            self.dashboard_page.click_availability_link()
            # Add assertions or further steps after clicking availability link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click availability link: {e}")

    def test_click_notification_link(self):
        try:
            self.dashboard_page.click_notification_link()
            # Add assertions or further steps after clicking notification link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click notification link: {e}")

    def test_click_Bid_link(self):
        try:
            self.dashboard_page.click_Bid_link()
            # Add assertions or further steps after clicking bid link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click Bid link: {e}")

    def test_click_Punch_link(self):
        try:
            self.dashboard_page.click_Punch_link()
            # Add assertions or further steps after clicking punch link
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.fail(f"Failed to click Punch link: {e}")


if __name__ == "__main__":
    unittest.main()
