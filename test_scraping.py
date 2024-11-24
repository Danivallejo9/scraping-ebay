# test_scraping.py
import unittest
from scraping_ebay import main_function  # Importa la función que ejecuta el scraping

class TestScraping(unittest.TestCase):
    def test_scraping(self):
        """Verifica que el scraping devuelva resultados"""
        # Ejecuta el scraping
        data = main_function()  # Llama a la función que hace el scraping y retorna datos

        # Verifica que haya productos en los resultados
        self.assertGreater(len(data), 0, "No se encontraron productos")

    def test_no_null_values(self):
        """Verifica que no haya valores nulos en los productos y precios"""
        # Ejecuta el scraping
        data = main_function()

        # Verifica que no haya valores nulos
        self.assertTrue(all(producto for producto in data['Producto']), "Hay productos nulos o vacíos")
        self.assertTrue(all(precio for precio in data['Precio']), "Hay precios nulos o vacíos")

    def test_column_names(self):
        """Verifica que las columnas del DataFrame sean las esperadas"""
        # Ejecuta el scraping
        data = main_function()

        # Verifica que las columnas sean 'Producto' y 'Precio'
        self.assertListEqual(list(data.columns), ['Producto', 'Precio'], "Las columnas no coinciden con las esperadas")

    def test_minimum_results(self):
        """Verifica que al menos haya 5 productos"""
        # Ejecuta el scraping
        data = main_function()

        # Verifica que haya al menos 5 resultados
        self.assertGreaterEqual(len(data), 5, "Se esperaban al menos 5 productos")

if __name__ == '__main__':
    unittest.main()
