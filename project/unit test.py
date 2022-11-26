# unit test

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


class Google_search(unittest.TestCase):
    @classmethod
    def Set_upClass(self):
        self.Ser = Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
        self.Driver = webdriver.Chrome(service=self.Ser)
    def Test_search(self):
        self.Driver.get("https://www.google.com/")
        self.Driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("Automation testing")
        self.Driver.find_element(By.XPATH, "//input[@class='gNO89b']").click()

    # @classmethod
    def tearDownClass(self):
        self.Driver.quit()
        print("Test Pass")
test=Google_search()
test.setUpClass()
test.Test_search()
test.tearDownClass()


