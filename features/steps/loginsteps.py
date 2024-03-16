from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# from selenium.webdriver.remote.webdriver import WebDriver


@given('I launch Chrome browser')
def openBrowser(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when('I open orange HRM homepage')
def openHome(self):
    self.driver.get("https://practicetestautomation.com/practice-test-login/")


@when('Enter username "{user}" and password "{pwd}"')
def enterCredentials(self, user, pwd):
    self.driver.find_element(By.ID, "username").send_keys(user)
    self.driver.find_element(By.ID, "password").send_keys(pwd)


@when('Click on login button')
def clickSubmit(self):
    self.driver.find_element(By.ID, "submit").click()


@then('User must successfully login to the Dashboard page')
def step_impl(self):
    # text = self.driver.find_element(By.TAG_NAME, "h1").text()
    # text = self.driver.find_element(By.TAG_NAME, "h1").text
    # assert text == "Logged In Successfully"
    # self.driver.close()

    try:
        # text = self.driver.find_element(By.TAG_NAME, "h1").text()
        text = self.driver.find_element(By.TAG_NAME, "h1").text
    except:
        self.driver.close()
        assert False, "Test Failed"

    if text == "Logged In Successfully":
        self.driver.close()
        assert True, "Test Passed"
