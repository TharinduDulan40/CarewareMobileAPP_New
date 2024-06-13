import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
import HTMLTestRunner


class TestSchedule(unittest.TestCase):  # Changed Test_Schedule to TestSchedule to follow naming conventions

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("chivarkey", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(2)
        self.dashboard_page.click_schedule_link()

    def tearDown(self):
        self.driver.quit()

    def test_schedule_view(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#secondary_header_window_title"))
        )

        # Check if the element is found
        if element:
            print("You're in the schedule page")
        else:
            print("Please visit the schedule page")

    def test_backward_navigating_schedule(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "moveBackward")
        try:
            # Check if the element for navigating backward is present
            move_backward_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "moveBackward"))
            )
            # Get the current month displayed before navigation
            current_month_element = self.driver.find_element(By.ID, "monthLabel")
            current_month_before = current_month_element.text
            time.sleep(2)
            # If the element is found, simulate clicking it
            move_backward_button.click()
            # Get the current month displayed after navigating backward
            current_month_after = current_month_element.text
            # Assert that the month has changed after clicking the backward button
            self.assertNotEqual(current_month_before, current_month_after,
                                "Month did not change after navigating backward")
            print(f"Successfully navigated to the previous month. Current month: {current_month_after}")
            # Here, you can perform further assertions or verifications related to the month change

        except NoSuchElementException:
            # If the element is not found, print a message indicating absence
            print("Button to navigate backward not found. Unable to move to the previous month.")

    def test_move_forward_navigation_link(self):
        try:
            # Wait for the move forward button to be clickable
            move_forward_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "moveForward"))
            )
            # Get the current month displayed before navigation
            current_month_element = self.driver.find_element(By.ID, "monthLabel")
            current_month_before = current_month_element.text
            # If the element is found, simulate clicking it
            move_forward_button.click()
            # Get the current month displayed after navigating forward
            current_month_after = current_month_element.text
            # Assert that the month has changed after clicking the forward button
            self.assertNotEqual(current_month_before, current_month_after,
                                "Month did not change after navigating forward")
            print(f"Successfully navigated to the next month. Current month: {current_month_after}")
            # Here, you can perform further assertions or verifications related to the month change

        except NoSuchElementException:
            # If the element is not found, print a message indicating absence
            print("Button to navigate forward not found. Unable to move to the next month.")

    def test_schedule_view_Detail_screen(self):
        time.sleep(2)
        try:
            schedule_detail_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "0-0"))
            )
            # If the element is found, click it
            time.sleep(2)
            if schedule_detail_element:
                schedule_detail_element.click()
                print("navigated to schedule view screen")
                time.sleep(2)
            else:
                print("Schedule detail list container not found")

        except Exception as e:
            print(f"Error: {e}")
            self.fail(
                "Element 'schedule_detail_list_container' not found. You might not be in the schedule view screen.")

    def test_availability_link(self):
        self.test_schedule_view()
        self.test_schedule_view_Detail_screen()
        self.driver.find_element(By.CLASS_NAME, "linkTitleContainer").click()
        time.sleep(2)
        add_availability_element = self.driver.find_element(By.ID, "secondary_header_window_title")
        if add_availability_element:
            print("You're in Add Availability page")
        else:
            print("Add Availability element not found")

        time.sleep(2)

    def test_Leaverequest_link(self):
        self.test_schedule_view()
        self.test_schedule_view_Detail_screen()
        self.driver.find_element(By.CLASS_NAME, "linkTitleContainer").click()
        time.sleep(2)
        add_availability_element = self.driver.find_element(By.ID, "secondary_header_window_title")
        if add_availability_element:
            print("You're in Add leave request Page")
        else:
            print("Add Availability element not found")

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
