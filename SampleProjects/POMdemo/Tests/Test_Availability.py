import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
from SampleProjects.POMdemo.Pages.Availability_Page import AvailabilityPage


class TestAvailability(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.delay_time = 2

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("kk116402", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(2)  # Global delay before clicking the availability link

    def tearDown(self):
        time.sleep(self.delay_time)  # Global delay after each test
        self.driver.quit()

    def test_overlapping_assignment_message(self):
        time.sleep(2)
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate overlapping assignment scenario
        time.sleep(2)
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for overlapping assignment
        message_text = self.availability_page.handle_message_box()
        if "overlaps with current assignment(s)" in message_text.lower():
            print("Overlapping assignment message handled correctly.")
        else:
            self.fail("Overlapping assignment message not handled properly")

    def test_missing_availability_type_message(self):
        time.sleep(2)
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate missing availability type scenario
        # Do not select availability type and attempt to submit
        time.sleep(2)
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for missing availability type
        message_text = self.availability_page.handle_message_box()
        if "please enter a valid availability type" in message_text.lower():
            print("Missing availability type message handled correctly.")
        else:
            self.fail("Missing availability type message not handled properly")

    def test_missing_shift_selection_message(self):
        time.sleep(2)
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate missing shift selection scenario
        time.sleep(2)
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        # Do not select any shift and attempt to submit
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for missing shift selection
        message_text = self.availability_page.handle_message_box()
        if "please select at-least one shift" in message_text.lower():
            print("Missing shift selection message handled correctly.")
        else:
            self.fail("Missing shift selection message not handled properly")

    def test_successful_availability_addition(self):
        time.sleep(2)
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Provide correct inputs for successful addition
        time.sleep(2)
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-07-12")
        self.availability_page.set_end_date("2024-07-12")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for successful addition
        message_text = self.availability_page.handle_message_box()
        if "your changes were saved" in message_text.lower():
            print("Successful availability addition message handled correctly.")
        else:
            self.fail("Successful availability addition message not handled properly")

    def test_successful_unavailability_addition(self):
        time.sleep(2)
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Provide correct inputs for successful addition
        time.sleep(2)
        self.availability_page.select_availability_type("unavail")
        self.availability_page.set_start_date("2024-07-17")
        self.availability_page.set_end_date("2024-07-17")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for successful addition
        message_text = self.availability_page.handle_message_box()
        if "your changes were saved" in message_text.lower():
            print("Successful unavailability addition message handled correctly.")
        else:
            self.fail("Successful unavailability addition message not handled properly")


if __name__ == "__main__":
    unittest.main()
