import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage


class TestLeave(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("bskaria", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(2)
        self.dashboard_page.click_leave_request_link()
        #

    def tearDown(self):
        self.driver.quit()

    def test_leave_request(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
        )

        if element:
            print("You're in the Leave request page")
        else:
            print("Please visit the Leave request page")

    def test_navigate_AddRequest(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "btnNew").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
        )
        if element:
            print("You're in the Leave request page")
        else:
            print("Please visit the Leave request page")

    def test_select_leaveType_sick(self):
        time.sleep(2)
        self.test_navigate_AddRequest()
        self.dropdown_element = self.driver.find_element(By.ID, "leave_type")
        dropdown = Select(self.dropdown_element)

        dropdown.select_by_visible_text("SICK LEAVE")
        selected_option = dropdown.first_selected_option.text
        self.assertEqual(selected_option, "SICK LEAVE")
        print(f"You selected leave type as {selected_option}")

    def test_select_leaveType_off(self):
        time.sleep(2)
        self.test_navigate_AddRequest()
        self.dropdown_element = self.driver.find_element(By.ID, "leave_type")
        dropdown = Select(self.dropdown_element)

        dropdown.select_by_visible_text("Off")
        time.sleep(2)
        selected_option = dropdown.first_selected_option.text
        self.assertEqual(selected_option, "Off")
        print(f"You selected leave type as {selected_option}")

    def test_select_start_date(self):
        start_date = self.driver.find_element(By.ID, "start_date")
        start_date.click()
        start_date.clear()
        start_date.send_keys("2023-12-31")

    def test_select_end_date(self):
        end_date = self.driver.find_element(By.ID, "end_date")
        end_date.click()
        end_date.clear()
        end_date.send_keys("2024-01-07")

    def test_add_sick_leave(self):
        time.sleep(2)
        self.test_navigate_AddRequest()
        self.test_select_leaveType_sick()
        self.test_select_start_date()
        self.test_select_end_date()

        comment = self.driver.find_element(By.ID, "comment")
        comment.clear()
        comment.send_keys("Test1")

        submit = self.driver.find_element(By.ID, "btnAddLeave")
        submit.click()
        # add sick leave logic

    def test_add_off_leave(self):
        time.sleep(2)
        self.test_navigate_AddRequest()
        self.test_select_leaveType_off()
        self.test_select_start_date()
        self.test_select_end_date()
        comment = self.driver.find_element(By.ID, "comment")
        comment.clear()
        comment.send_keys("Test2")

        submit = self.driver.find_element(By.ID, "btnAddLeave")
        submit.click()
        self.test_alert_message()

    def test_alert_message(self):
        try:
            alert_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='messagebox_body']/p[text()='Your leave request was placed successfully!']"))
            )
            if alert_message:
                print("Your leave request was placed successfully!")
            else:
                print("your leave request not placed successfully")
        except Exception as e:
            print("Exception occurred:", e)


if __name__ == "__main__":
    unittest.main()
