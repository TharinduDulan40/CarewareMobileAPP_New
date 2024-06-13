import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  # You need to have Chrome installed or use any other supported browser
    yield driver
    driver.quit()


def test_google_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    assert "Python" in browser.title
    assert "No results found." not in browser.page_source


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output="C:\\Users\\User\\PycharmProjects\\PageobjectModel\\SampleProjects"
                                                   "\\POMdemo\\Tests\\reports"))

