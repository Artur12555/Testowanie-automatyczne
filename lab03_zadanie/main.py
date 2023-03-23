def test_page_load():
    driver = webdriver.Chrome("C:/Users/Admin/chromedriver.exe")
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.quit()

def test_login():
    driver = webdriver.Chrome("C:/Users/Admin/chromedriver.exe")
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.find_element(By.NAME, 'user-name').send_keys("standard_user")
    driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Swag Labs" in driver.title
    driver.find_element(By.CSS_SELECTOR, ".bm-burger-button").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "Swag Labs" in driver.title
    driver.quit()

def test_find_element_and_text():
    driver = webdriver.Chrome("C:/Users/Admin/chromedriver.exe")
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.find_element(By.NAME, 'user-name').send_keys("standard_user")
    driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    assert "Swag Labs" in driver.title
    element = driver.find_element(By.CSS_SELECTOR, ".product_label")
    assert element.text == "Products"
    driver.find_element(By.CSS_SELECTOR, ".bm-burger-button").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "Swag Labs" in driver.title
    driver.quit()
    
def test_scenario1():
    test_page_load()

def test_scenario2():
    test_login()

def test_scenario3():
    test_find_element_and_text()
