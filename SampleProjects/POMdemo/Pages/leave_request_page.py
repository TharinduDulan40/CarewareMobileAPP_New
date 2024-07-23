from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LeaveRequestPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_request_button = (By.ID, "btnNew")
        self.leave_type_dropdown = (By.ID, "leave_type")
        self.start_date_field = (By.ID, "start_date")
        self.end_date_field = (By.ID, "end_date")
        self.comment_field = (By.ID, "comment")
        self.alert_message_body = (By.XPATH, "//*[@id='messagebox_body']")
        self.alert_message = (
            By.XPATH, "//div[@id='messagebox_body']/p[text()='Your leave request was placed successfully!']")

    def click_add_request(self):
        self.driver.find_element(*self.add_request_button).click()

    def select_leave_type(self, leave_type):
        dropdown = Select(self.driver.find_element(*self.leave_type_dropdown))
        dropdown.select_by_visible_text(leave_type)

    def set_start_date(self, date):
        start_date = self.driver.find_element(By.ID, "start_date")
        start_date.click()
        start_date.clear()
        start_date.send_keys(date)

    def set_end_date(self, date):
        end_date = self.driver.find_element(By.ID, "end_date")
        end_date.click()
        end_date.clear()
        end_date.send_keys(date)

    def add_comment(self, comment):
        comment_field = self.driver.find_element(By.ID, "comment")
        comment_field.clear()
        comment_field.send_keys(comment)

    def get_alert_message(self):
        return self.driver.find_element(*self.alert_message).text
