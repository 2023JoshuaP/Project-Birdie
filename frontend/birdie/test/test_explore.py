from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
driver = webdriver.Chrome()

try:
    # Navegar a la página Explore
    driver.get("http://localhost:3000/explore")  # Cambia esto si tu servidor usa otro puerto

    # Esperar a que el título de la página sea el correcto
    WebDriverWait(driver, 10).until(EC.title_is("Birdie | Explore"))
    print("Current page title:", driver.title)
    assert driver.title == "Birdie | Explore", f"Title mismatch: {driver.title}"

    # Verificar que se cargaron publicaciones iniciales
    posts = driver.find_elements(By.CLASS_NAME, "card")  # Cambia 'card' según la clase usada en CardContainer
    assert len(posts) > 0, "No se cargaron publicaciones iniciales"

    # Verificar que el formulario TweetForm está presente
    tweet_form = driver.find_element(By.TAG_NAME, "form")
    assert tweet_form is not None, "El formulario TweetForm no se encontró"

    # Probar el botón "more" para cargar más publicaciones
    more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'more')]")
    assert more_button is not None, "El botón 'more' no se encontró"
    more_button.click()

    time.sleep(2)  # Esperar a que se carguen más publicaciones

    # Verificar que se cargaron más publicaciones al hacer clic en "more"
    updated_posts = driver.find_elements(By.CLASS_NAME, "card")
    assert len(updated_posts) > len(posts), "No se cargaron más publicaciones al hacer clic en 'more'"

finally:
    driver.quit()
