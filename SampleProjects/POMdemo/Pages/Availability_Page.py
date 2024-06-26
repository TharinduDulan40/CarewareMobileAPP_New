import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AvailabilityPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_availability_button(self):
        add_availability_button = self.driver.find_element(By.XPATH, "//*[@id='btnAddAvail']")
        add_availability_button.click()

    def is_on_add_availability_page(self):
        try:
            header = self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Add Availability')]")
            return True
        except Exception as e:
            print(f"Exception checking page title: {e}")
            return False

    def select_availability_type(self, availability_type):
        availability_type_dropdown = self.driver.find_element(By.ID, 'availTypeSelect')
        availability_type_dropdown.click()
        time.sleep(1)  # Replace with WebDriverWait if necessary
        option = self.driver.find_element(By.XPATH, f"//option[@id='{availability_type.lower()}']")
        option.click()

    def set_start_date(self, date):
        start_date_input = self.driver.find_element(By.ID, 'start_date')
        start_date_input.clear()
        start_date_input.send_keys(date)

    def set_end_date(self, date):
        end_date_input = self.driver.find_element(By.ID, 'end_date')
        end_date_input.clear()
        end_date_input.send_keys(date)

    def select_time_toggle(self, toggle_id):
        toggle = self.driver.find_element(By.ID, toggle_id)
        toggle.click()

    def add_comment(self, comment):
        comment_input = self.driver.find_element(By.ID, 'comment')
        comment_input.clear()
        comment_input.send_keys(comment)

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.ID, 'btnAdd')
        submit_button.click()

        # Wait for success or error message to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'messagebox_body'))
        )

    def handle_message_box(self):
        try:
            message_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'messagebox_body'))
            )
            message_text = message_box.text.strip()
            ok_button = self.driver.find_element(By.ID, 'messagebox_btn$0')
            ok_button.click()
            return message_text
        except Exception as e:
            print(f"Error handling message box: {e}")
            return None
