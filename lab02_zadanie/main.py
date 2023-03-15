from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    #Open the web page
    driver = webdriver.Chrome("C:/Users/Admin/chromedriver.exe")
    driver.get("https://www.saucedemo.com")

    #Test case 1: Test the page title
    assert "Swag Labs" in driver.title

    #Test case 2: Test the existence of login form fields
    assert driver.find_element(By.NAME, 'user-name')
    assert driver.find_element(By.NAME, 'password')

    #Test case 3: Test invalid username and password combination
    username = "invalidusername"
    password = "invalidpassword"
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

    #Test case 4: Test invalid username with valid password
    username = "invalidusername"
    password = "secret_sauce"
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

    #Test case 5: Test valid username with invalid password
    username = "standard_user"
    password = "invalidpassword"
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

    #Test case 6: Test successful login
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Swag Labs" in driver.title

    #Test case 7: Test logout functionality
    driver.find_element(By.CSS_SELECTOR, ".bm-burger-button").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "Swag Labs" in driver.title

    #Test case 8: Test invalid input for username and password fields
    username = "[]"
    password = "[]"
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

finally:
    driver.quit()