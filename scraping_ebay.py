# -*- coding: utf-8 -*-
"""Vallejo_Daniela_Analizando_EA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AshFR_9-O2SJEBX0ZOD5csq8aWxTEkDB
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def main_function():
    # Configuración del navegador en modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Modo headless para CI/CD
    chrome_options.add_argument("--no-sandbox")  # Requerido para entornos de CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Mejora estabilidad en contenedores
    chrome_options.add_argument("--disable-gpu")  # Opcional en entornos gráficos
    driver = webdriver.Chrome(options=chrome_options)

    # URL base de scraping
    driver.get('https://www.ebay.com/sch/i.html?_nkw=smartwatch')

    # Pausa para cargar elementos
    time.sleep(5)

    # Inicialización de listas para almacenar los resultados
    productos = []
    precios = []

    while True:
        # Localiza los elementos de productos y precios
        items = driver.find_elements(By.CSS_SELECTOR, '.s-item__title') 
        prices = driver.find_elements(By.CSS_SELECTOR, '.s-item__price') 

        for item, price in zip(items, prices):
            productos.append(item.text)
            precios.append(price.text)

        # Intenta pasar a la página siguiente
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.pagination__next')  # Botón "Siguiente"
            next_button.click()
            time.sleep(5)  # Pausa para que la página cargue
        except Exception as e:
            # Sale del bucle si no hay más páginas
            print("No hay más páginas. Finalizando scraping.")
            break

    # Cierra el navegador
    driver.quit()

    # Devuelve los datos en formato DataFrame
    return pd.DataFrame({
        'Producto': productos,
        'Precio': precios
    })
