from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "txtUsername")
        self.password_input = (By.ID, "txtPassword")
        self.login_button = (By.TAG_NAME, "button")
        self.message_box_modal = (By.ID, "messagebox_modal")
        self.message_box_btn = (By.ID, "messagebox_btn$0")

    def login(self, username, password):
        self.driver.get("https://ksumcinternal.caresystemsinc.com/KSUMC_QA_Trunk/html_interface/staff/login.jsp")
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def handle_message_box(self):
        try:
            message_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.message_box_modal)
            )
            if message_box.is_displayed():
                proceed_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.message_box_btn)
                )
                proceed_button.click()
        except Exception as e:
            print(f"Error handling message box: {e}")
