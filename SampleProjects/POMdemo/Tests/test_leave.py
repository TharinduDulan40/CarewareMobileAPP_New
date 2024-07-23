import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from SampleProjects.POMdemo.Pages.Dashboard_Page import DashboardPage
from SampleProjects.POMdemo.Pages.leave_request_page import LeaveRequestPage


class TestLeave(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.login("kk116402", "admin")
        self.login_page.handle_message_box()
        self.dashboard_page = DashboardPage(self.driver)
        time.sleep(2)
        self.dashboard_page.click_leave_request_link()
        self.leave_request_page = LeaveRequestPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def submit_leave_request(self):
        self.driver.find_element(By.XPATH, "//*[@id='btnAddLeave']").click()

    def test1_leave_request(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
        )
        if element:
            print("You're in the Leave request page")
        else:
            print("Please visit the Leave request page")

    def test2_navigate_AddRequest(self):
        time.sleep(2)
        self.leave_request_page.click_add_request()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "secondary_header_window_title"))
        )
        if element:
            print("You're in the Leave request page")
        else:
            print("Please visit the Leave request page")

    def test3_select_leaveType_sick(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        time.sleep(2)
        self.leave_request_page.select_leave_type("SICK LEAVE")
        time.sleep(2)
        selected_option = Select(self.driver.find_element(By.ID, "leave_type")).first_selected_option.text
        self.assertEqual(selected_option, "SICK LEAVE")
        print(f"You selected leave type as {selected_option}")

    def test4_select_leaveType_off(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        self.leave_request_page.select_leave_type("Off")
        time.sleep(2)
        selected_option = self.driver.find_element(By.ID, "leave_type").get_attribute("value")
        self.assertEqual(selected_option, "Off")
        print(f"You selected leave type as {selected_option}")

    def test5_select_start_date(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        time.sleep(2)
        self.leave_request_page.set_start_date("2024-07-25")

    def test6_select_end_date(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        time.sleep(2)
        self.leave_request_page.set_end_date("2024-07-25")

    def test7_add_sick_leave(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        time.sleep(2)
        self.leave_request_page.select_leave_type("SICK LEAVE")
        time.sleep(2)
        self.leave_request_page.set_start_date("2024-07-28")
        self.leave_request_page.set_end_date("2024-07-28")
        time.sleep(2)
        self.leave_request_page.add_comment("Test1")
        time.sleep(2)
        self.submit_leave_request()
        time.sleep(2)

        # Verify alert message
        try:
            alert_message_body = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='messagebox_body']"))
            )
            if alert_message_body:
                print({alert_message_body.text})
            else:
                print("Alert message not found.")
        except Exception as e:
            print(f"Exception occurred while fetching alert message: {e}")

    def test8_add_off_leave(self):
        time.sleep(2)
        self.test2_navigate_AddRequest()
        time.sleep(2)
        self.leave_request_page.select_leave_type("Off")
        time.sleep(2)
        self.leave_request_page.set_start_date("2024-07-24")
        self.leave_request_page.set_end_date("2024-07-24")
        time.sleep(2)
        self.leave_request_page.add_comment("Test2")
        time.sleep(2)
        self.submit_leave_request()
        time.sleep(2)

        # Verify alert message
        try:
            alert_message_body = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='messagebox_body']"))
            )
            if alert_message_body:
                print({alert_message_body.text})
            else:
                print("Alert message not found.")
        except Exception as e:
            print(f"Exception occurred while fetching alert message: {e}")

    def test9_alert_message(self):
        try:
            alert_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='messagebox_body']/p[text()='Your leave request was placed successfully!']"))
            )
            if alert_message:
                print("Your leave request was placed successfully!")
            else:
                print("Your leave request was not placed successfully")
        except Exception as e:
            print("Exception occurred:", e)

    def test10_modify_leave_request(self):
        self.test1_leave_request()
        try:
            leave_items = self.driver.find_elements(By.XPATH, "//*[@id='leave$153']/div[2]")
            if not leave_items:
                print("No leaves available for modification.")
                return  # Exit the test if no leaves are available

            # Click on the 4th row leave (example: "SUN 28 SICK LEAVE 1 Day (s)")
            leave_item = self.driver.find_element(By.XPATH, "//div[@id='leave$152']//img")
            leave_item.click()

            # Verify the header after clicking on a leave item
            header_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='secondary_header_window_title']"))
            )
            header_text = header_element.text
            print(f"You navigated to {header_text} page")

            # Now run the add off leave request tes
        except Exception as e:
            print(f"Exception occurred during leave modification: {e}")

        self.test4_select_leaveType_off()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLeave("test1_leave_request"))
    suite.addTest(TestLeave("test2_navigate_AddRequest"))
    suite.addTest(TestLeave("test3_select_leaveType_sick"))
    suite.addTest(TestLeave("test4_select_leaveType_off"))
    suite.addTest(TestLeave("test5_select_start_date"))
    suite.addTest(TestLeave("test6_select_end_date"))
    suite.addTest(TestLeave("test7_add_sick_leave"))
    suite.addTest(TestLeave("test8_add_off_leave"))
    suite.addTest(TestLeave("test9_alert_message"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
