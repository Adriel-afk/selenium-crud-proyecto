from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Edge()
wait = WebDriverWait(driver, 20)


driver.get("file:///C:/Users/user/OneDrive/Desktop/selenium-crud-proyecto/web/index.html")


wait.until(EC.visibility_of_element_located((By.ID, "username")))

driver.save_screenshot("screenshots/01_pagina_abierta.png")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "loginBtn").click()

time.sleep(2)
driver.save_screenshot("screenshots/02_login_exitoso.png")


driver.find_element(By.ID, "nombre").send_keys("Juan")
driver.find_element(By.ID, "edad").send_keys("20")
driver.find_element(By.ID, "curso").send_keys("Informatica")
driver.find_element(By.ID, "guardar").click()

time.sleep(2)
driver.save_screenshot("screenshots/03_estudiante_creado.png")

driver.find_element(By.XPATH, "//button[text()='Eliminar']").click()

time.sleep(2)
driver.save_screenshot("screenshots/04_estudiante_eliminado.png")


driver.refresh()

wait.until(EC.visibility_of_element_located((By.ID, "username")))

driver.find_element(By.ID, "username").send_keys("wrong")
driver.find_element(By.ID, "password").send_keys("0000")
driver.find_element(By.ID, "loginBtn").click()

time.sleep(2)
driver.save_screenshot("screenshots/05_login_incorrecto.png")

driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "loginBtn").click()

time.sleep(2)
driver.save_screenshot("screenshots/06_campos_vacios.png")


time.sleep(5)  
driver.quit()