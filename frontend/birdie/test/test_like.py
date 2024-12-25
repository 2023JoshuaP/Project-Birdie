from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Iniciar el navegador (asegúrate de tener el driver adecuado para tu navegador)
driver = webdriver.Chrome()

# Abrir la URL
driver.get("http://localhost:3000/likes")

try:
    # Esperar a que el título de la página sea el esperado
    print("Esperando título...")
    WebDriverWait(driver, 10).until(
        EC.title_contains("Birdie | Liked Posts")
    )
    print("Título de la página es correcto:", driver.title)

    # Esperar a que al menos una publicación esté visible
    print("Esperando publicaciones...")
    WebDriverWait(driver, 10).until(
        lambda driver: len(driver.find_elements(By.CLASS_NAME, "card")) > 0
    )
    posts = driver.find_elements(By.CLASS_NAME, "card")
    print(f"Se encontraron {len(posts)} publicaciones.")

    # Opcional: Esperar a que el botón "more" esté disponible y hacer clic si es visible
    try:
        more_button = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='more']"))
        )
        print("Botón 'more' encontrado, haciendo clic...")
        more_button.click()

        # Esperar a que se carguen más publicaciones
        WebDriverWait(driver, 10).until(
            lambda driver: len(driver.find_elements(By.CLASS_NAME, "card")) > len(posts)
        )
        posts = driver.find_elements(By.CLASS_NAME, "card")
        print(f"Se encontraron {len(posts)} publicaciones después de cargar más.")
    except Exception as e:
        print("No se encontró el botón 'more' o no fue necesario interactuar con él.")

finally:
    # Imprimir el título actual para depuración
    print("Título final de la página:", driver.title)

    # Cerrar el navegador después de un breve retraso
    time.sleep(2)
    driver.quit()
