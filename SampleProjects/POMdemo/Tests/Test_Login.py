import time
import unittest
from selenium import webdriver
from SampleProjects.POMdemo.Pages.login_page import LoginPage
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        self.login_page.login("bskaria", "admin")
        self.login_page.handle_message_box()
        time.sleep(2)
        header_menu_btn = self.driver.find_element(By.CSS_SELECTOR, "#header_menu_btn")
        header_menu_btn.click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(1) div.container-fluid div.row:nth-child(1) div:nth-child(3) > "
                                 "button:nth-child(1)").click()
        print("Test completed")
        # Add assertions or further steps after login

    def test_invalid_login(self):
        self.login_page.login("invalid_user", "invalid_password")
        self.login_page.handle_message_box()
        # Add assertions or further steps for invalid login handling


if __name__ != "__main__":
    pass
else:
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='reports'))

# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestLogin))
#     dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
#     runner = HTMLTestRunner(open_in_browser=True)
#     runner.run(suite)
