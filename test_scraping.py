# test_scraping.py
import unittest
from scraping_ebay import main_function  # Importa la función que ejecuta el scraping

class TestScraping(unittest.TestCase):
    def test_scraping(self):
        # Ejecuta el scraping
        data = main_function()  # Llama a la función que hace el scraping y retorna datos

        # Verifica que haya productos en los resultados
        self.assertGreater(len(data), 0, "No se encontraron productos")

    def test_no_null_values(self):
        # Verifica que no haya valores nulos en los productos y precios
        data = main_function()
        self.assertTrue(all(producto is not None for producto in data['Producto']))
        self.assertTrue(all(precio is not None for precio in data['Precio']))

if __name__ == '__main__':
    unittest.main()
