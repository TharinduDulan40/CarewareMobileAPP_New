import time
import unittest
from selenium import webdriver
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

    def handle_modal_message(self, expected_message):
        message_text = self.availability_page.handle_message_box()
        if expected_message.lower() in message_text.lower():
            print(f"{expected_message} handled correctly.")
        else:
            self.fail(f"{expected_message} not handled properly")

    def test_overlapping_assignment_message(self):
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate overlapping assignment scenario
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for overlapping assignment
        self.handle_modal_message("overlaps with current assignment(s)")

    def test_missing_availability_type_message(self):
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate missing availability type scenario
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for missing availability type
        self.handle_modal_message("please enter a valid availability type")

    def test_missing_shift_selection_message(self):
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Simulate missing shift selection scenario
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-06-26")
        self.availability_page.set_end_date("2024-06-27")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for missing shift selection
        self.handle_modal_message("please select at-least one shift")

    def test_successful_availability_addition(self):
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)
        self.availability_page.click_add_availability_button()

        # Provide correct inputs for successful addition
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-07-12")
        self.availability_page.set_end_date("2024-07-12")
        self.availability_page.select_time_toggle("0")
        self.availability_page.add_comment("Test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for successful addition
        self.handle_modal_message("your changes were saved")

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
        self.handle_modal_message("your changes were saved")

        # Additional scenarios for unavailability
        # time.sleep(2)
        # self.dashboard_page.click_availability_link()
        # self.test_overlapping_assignment_message()
        # self.dashboard_page.click_availability_link()
        # self.test_missing_availability_type_message()
        # self.dashboard_page.click_availability_link()
        # self.test_missing_shift_selection_message()

    def test_modify_availability(self):
        self.dashboard_page.click_availability_link()
        self.availability_page = AvailabilityPage(self.driver)

        # Locate the specific availability element to edit
        self.availability_page.click_edit_icon("avail$1")

        # Now on the modify availability page, modify the details
        self.availability_page.select_availability_type("avail")
        self.availability_page.set_start_date("2024-08-01")
        self.availability_page.set_end_date("2024-08-02")
        self.availability_page.select_time_toggle("1")
        self.availability_page.add_comment("Modified test comment")
        self.availability_page.click_submit_button()

        # Handle modal message for successful modification
        self.handle_modal_message("your changes were saved")

        # use above test scenarios to handle other messages
        # time.sleep(2)
        # self.dashboard_page.click_availability_link()
        # self.availability_page.click_edit_icon("avail$1")
        # self.test_overlapping_assignment_message()
        # self.dashboard_page.click_availability_link()
        # self.test_missing_availability_type_message()
        # self.dashboard_page.click_availability_link()
        # self.test_missing_shift_selection_message()


if __name__ == "__main__":
    unittest.main()
