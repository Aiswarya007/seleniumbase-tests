# from behave import given
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@given('launch chrome browser')
def launchBrowser(self):
    # self.driver = webdriver.Chrome(executable_path = "C:\Users\aiswa\Selenium_Projects\Drivers\chrome-win64\chrome.exe")
    # add the drivers inside C:\Users\aiswa\AppData\Local\Programs\Python\Python311\Scripts and set environment variable for this folder and use below line
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when('open orange hrm homepage')
def openHomePage(self):
    self.driver.get("https://practicetestautomation.com/practice-test-login/")


@then('verify that the logo present on Page')
def verifyLogo(self):
    status = self.driver.find_element(By.XPATH, "//div[@id='site-title']//img[@alt='Practice Test Automation']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(self):
    self.driver.close()
