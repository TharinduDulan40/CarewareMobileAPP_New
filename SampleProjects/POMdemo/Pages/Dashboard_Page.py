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
            By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div[2]/a/div/div[1]/img'
        )
        leave_request_link.click()

    def click_availability_link(self):
        availability_link = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[4]/div[1]/div[3]/a/div/div[1]/img"

        )
        availability_link.click()

    def click_notification_link(self):
        notification_link = self.driver.find_element(
            By.CSS_SELECTOR, 'img[alt=\'Image Description\']'
        )
        notification_link.click()

    def click_Bid_link(self):
        Bid_link = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > "
            "a:nth-child(1) > div:nth-child(1) > div:nth-child(2)"
        )
        Bid_link.click()

    def click_Punch_link(self):
        Punch_link = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[4]/div[2]/div[3]/a/div/div[2]/span"
        )
        Punch_link.click()

    # Add other methods for interacting with the dashboard as needed
