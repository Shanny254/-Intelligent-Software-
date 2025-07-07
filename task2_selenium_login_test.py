
# Task 2: Automated Login Testing with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (Ensure correct driver is installed for your browser)
driver = webdriver.Chrome()  # or webdriver.Firefox()

# URL of your login page
login_url = "http://example.com/login"
driver.get(login_url)

# Test Case 1: Valid credentials
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.ID, "loginBtn")

username_input.send_keys("valid_user")
password_input.send_keys("valid_password")
login_button.click()

time.sleep(2)
print("Valid Login Test:", "Success" if "dashboard" in driver.current_url else "Failed")

# Test Case 2: Invalid credentials
driver.get(login_url)
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.ID, "loginBtn")

username_input.send_keys("invalid_user")
password_input.send_keys("wrong_password")
login_button.click()

time.sleep(2)
error_message = driver.find_elements(By.CLASS_NAME, "error")
print("Invalid Login Test:", "Error Shown" if error_message else "Failed")

driver.quit()
