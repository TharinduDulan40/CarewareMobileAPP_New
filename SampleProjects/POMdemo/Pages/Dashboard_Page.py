from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_schedule_link(self):
        schedule_link = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.container-fluid div.row.justify-content-evenly.px-4:nth-child(1) "
            "div.col.p-2:nth-child(1) a.shortcut-link-path div.linkContainer > "
            "div.linkTitleContainer"
        )
        schedule_link.click()

    def click_leave_request_link(self):
        leave_request_link = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.container-fluid div.row.justify-content-evenly.px-4:nth-child(1) div.col.p-2:nth-child(3) "
            "a.shortcut-link-path div.linkContainer div.linkTitleContainer > span.customFont.shortcut-title"
        )
        leave_request_link.click()

    def click_availability_link(self):
        availability_link = self.driver.find_element(
            By.CSS_SELECTOR,
            'div.container-fluid div.row.justify-content-evenly.px-4:nth-child(2) div.col.p-2:nth-child(1) '
            'a.shortcut-link-path div.linkContainer div.linkTitleContainer > span.customFont.shortcut-title'
        )
        availability_link.click()

    def click_notification_link(self):
        notification_link = self.driver.find_element(
            By.CLASS_NAME, 'h-75'
        )
    # Add other methods for interacting with the dashboard as needed
