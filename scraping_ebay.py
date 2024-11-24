# -*- coding: utf-8 -*-
"""Vallejo_Daniela_Analizando_EA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AshFR_9-O2SJEBX0ZOD5csq8aWxTEkDB
"""



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
import pandas as pd

# Instalar automáticamente el ChromeDriver
chromedriver_autoinstaller.install()

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Modo sin cabeza (sin interfaz gráfica)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Inicializar el servicio
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Acceder a la página de eBay
driver.get('https://www.ebay.com/sch/i.html?_nkw=smartwatch')

# Esperar a que se cargue la página inicial
time.sleep(5)

# Listas para almacenar los resultados
productos = []
precios = []

# Extraer datos de las páginas
while True:
    # Extraer elementos en la página actual
    items = driver.find_elements(By.CSS_SELECTOR, '.s-item__title')
    prices = driver.find_elements(By.CSS_SELECTOR, '.s-item__price')

    # Guardar los datos en las listas
    for item, price in zip(items, prices):
        productos.append(item.text)
        precios.append(price.text)

    # Navegar a la siguiente página
    try:
        # Encontrar el botón "Siguiente" y hacer clic
        next_button = driver.find_element(By.CSS_SELECTOR, '.pagination__next')
        next_button.click()

        # Esperar a que la siguiente página se cargue
        time.sleep(5)
    except Exception as e:
        print(f"No se puede ir a la siguiente página: {e}")
        break  # Salir si no hay más páginas

# Convertir los resultados a un DataFrame
smartwatch = pd.DataFrame({
    'Producto': productos,
    'Precio': precios
})

# Mostrar el DataFrame
print(smartwatch)

# Exportar a un archivo CSV
smartwatch.to_csv('ebay_smartwatches.csv', index=False)

# Cerrar el navegador
driver.quit()

smartwatch.info()

smartwatch