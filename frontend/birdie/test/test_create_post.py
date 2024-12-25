from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

CHROME_DRIVER_PATH = "D:/Ingenieria de Software 2/chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

def test_create_post():
    try:
        driver.get("http://localhost:3000/signin")
        assert "Sign In To Birdie" in driver.title, "Unexpected page title!"
        
        # Login process
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "password")
        
        username_input.send_keys("Admin")
        password_input.send_keys("epcc2022")
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.title_contains("Home"))
        print("Login successful!")
        
        # Create post process
        post_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main-tweet-form"))
        )
        post_input.send_keys("Post de prueba desde Selenium!!!")
        
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Post']"))
        )
        post_button.click()
        
        time.sleep(2)
        print("Post created successfully!")
    except AssertionError as ae:
        print(f"Assertion failed: {ae}")
    except Exception as e:
        print(f"Error during test execution: {e}")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    test_create_post()