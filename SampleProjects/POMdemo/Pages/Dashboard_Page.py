from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_schedule_link(self):
        self._click_element(By.CSS_SELECTOR, "div.container-fluid div.row.justify-content-evenly.px-4:nth-child(1) "
                                             "div.col.p-2:nth-child(1) a.shortcut-link-path div.linkContainer > "
                                             "div.linkTitleContainer")

    def click_leave_request_link(self):
        self._click_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div[2]/a/div/div[1]/img')

    def click_availability_link(self):
        self._click_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div[3]/a/div/div[2]/span")

    def click_notification_link(self):
        self._click_element(By.CSS_SELECTOR, 'img[alt=\'Image Description\']')

    def click_Bid_link(self):
        self._click_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > "
                                             "div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > "
                                             "div:nth-child(1) > div:nth-child(2)")

    def click_Punch_link(self):
        self._click_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[3]/a/div/div[2]/span")

    def _click_element(self, by_locator, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by_locator, locator))
            )
            element.click()
        except NoSuchElementException as e:
            print(f"Element with locator '{locator}' not found: {e}")
            raise e
        except ElementNotInteractableException as e:
            print(f"Element with locator '{locator}' not intractable: {e}")
            raise e
        except TimeoutException as e:
            print(f"Timeout waiting for element with locator '{locator}' to be clickable: {e}")
            raise e
        except Exception as e:
            print(f"Exception occurred while clicking element with locator '{locator}': {e}")
            raise e
