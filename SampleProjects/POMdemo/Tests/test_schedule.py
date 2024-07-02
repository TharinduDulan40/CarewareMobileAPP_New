import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage  # Fixed import statement


class TestSchedule(unittest.TestCase):

    def setUp(self):
        # Set up Firefox browser for testing
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # Implicit wait
        self.driver.maximize_window()  # Maximize the browser window
        self.login_page = LoginPage(self.driver)
        self.login_page.login("kk116402", "admin")  # Perform login
        self.login_page.handle_message_box()  # Handle any message boxes
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(2)
        self.dashboard_page.click_schedule_link()  # Navigate to the schedule page

    def tearDown(self):
        # Quit the browser after each test
        self.driver.quit()

    def test1_schedule_view(self):
        # Test for checking if the schedule page is loaded
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='secondary_header_window_title']"))
        )
        if element:
            print("You're on the schedule page")
        else:
            print("Please visit the schedule page")

    def test2_backward_navigating_schedule(self):
        # Test for navigating backward in the schedule
        time.sleep(2)
        try:
            move_backward_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "moveBackward"))
            )
            current_month_element = self.driver.find_element(By.ID, "monthLabel")
            current_month_before = current_month_element.text
            time.sleep(2)
            move_backward_button.click()  # Click the backward button
            time.sleep(2)
            current_month_after = current_month_element.text
            self.assertNotEqual(current_month_before, current_month_after,
                                "Month did not change after navigating backward")
            print(f"Successfully navigated to the previous month. Current month: {current_month_after}")

        except NoSuchElementException:
            print("Button to navigate backward not found. Unable to move to the previous month.")

    def test3_forward_navigating_schedule(self):
        # Test for navigating forward in the schedule
        time.sleep(2)
        try:
            move_forward_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "moveForward"))
            )
            current_month_element = self.driver.find_element(By.ID, "monthLabel")
            current_month_before = current_month_element.text
            time.sleep(2)
            move_forward_button.click()  # Click the forward button
            time.sleep(2)
            current_month_after = current_month_element.text
            self.assertNotEqual(current_month_before, current_month_after,
                                "Month did not change after navigating forward")
            print(f"Successfully navigated to the next month. Current month: {current_month_after}")

        except NoSuchElementException:
            print("Button to navigate forward not found. Unable to move to the next month.")

    def test4_schedule_view_detail_screen(self):
        # Test for navigating to the schedule detail screen
        time.sleep(2)
        try:
            schedule_detail_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "0-0"))
            )
            time.sleep(2)
            if schedule_detail_element:
                schedule_detail_element.click()
                print("Navigated to schedule detail view screen")
                time.sleep(2)
            else:
                print("Schedule detail list container not found")

        except Exception as e:
            print(f"Error: {e}")
            self.fail(
                "Element 'schedule_detail_list_container' not found. You might not be in the schedule view screen.")

    def test5_availability_link(self):
        # Test for navigating to the availability page
        try:
            self.test1_schedule_view()
            self.test4_schedule_view_detail_screen()
            availability_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Availability')]"))
            )
            availability_element.click()
            time.sleep(2)
            add_availability_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
            )
            if add_availability_element:
                print("You're on the Add Availability page")
            else:
                print("Add Availability element not found")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def test6_bid_link(self):
        # Test for navigating to the bids page
        try:
            self.test1_schedule_view()
            self.test4_schedule_view_detail_screen()
            bids_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Bids')]"))
            )
            bids_element.click()
            time.sleep(2)
            add_bid_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
            )
            if add_bid_element:
                print("You're on the Bids page")
            else:
                print("Bids element not found")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")


if __name__ == '__main__':
    unittest.main()
