from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "D:/Ingenieria de Software 2/chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

def login():
    """Función para iniciar sesión en la aplicación."""
    driver.get("http://localhost:3000/signin")
    assert "Sign In To Birdie" in driver.title, "Unexpected page title!"
    print("Page title is correct!")

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

def test_explore():
    try:
        login()
        
        driver.get("http://localhost:3000/explore")
        assert "Birdie | Explore" in driver.title, "Unexpected page title!"
        print("Page Title passed!")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//img[contains(@class, 'rounded-xl')]"))
        )
        print("Publicaciones encontradas en el feed de Explore.")
    except AssertionError as ae:
        print(f"Assertion failed: {ae}")
    except Exception as e:
        print(f"Error during test execution: {e}")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    test_explore()