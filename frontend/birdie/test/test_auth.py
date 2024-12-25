from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

# Configuración del WebDriver
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:3000/auth")  # Ruta de autenticación

    # Prueba: Inicio de sesión con credenciales incorrectas
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("testuser")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("testpassword" + Keys.RETURN)

    time.sleep(2)  # Esperar redirección o alerta

    # Verificar si el inicio de sesión fue exitoso
    if "dashboard" in driver.current_url:
        # Mostrar una alerta de éxito
        driver.execute_script("alert('Inicio de sesión exitoso. Bienvenido al dashboard!');")
        time.sleep(3)  # Pausa para que se pueda leer la alerta

    else:
        # Manejar la alerta en caso de credenciales inválidas
        alert = Alert(driver)
        alert_text = alert.text  # Capturar el texto de la alerta
        print(f"Texto de la alerta: {alert_text}")
        assert "Invalid Login Credentials" in alert_text  # Verificar el mensaje
        alert.accept()  # Cerrar la alerta

finally:
    driver.quit()  # Cerrar el navegador
