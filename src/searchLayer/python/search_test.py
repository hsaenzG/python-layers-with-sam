import unittest
from  search import buscar_expresion_regular
import re

class calculation_test(unittest.TestCase):


    def test_buscar_expresion_regular(self):
        # Caso de prueba 1: Patrón simple que coincide
        resultado = buscar_expresion_regular("Hola mundo", r"mundo")
        assert resultado == True, f"Fallo en el caso de prueba 1. Se esperaba True, pero se obtuvo {resultado}"

        # Caso de prueba 2: Patrón que no coincide
        resultado = buscar_expresion_regular("Python es genial", r"Java")
        assert resultado == False, f"Fallo en el caso de prueba 2. Se esperaba False, pero se obtuvo {resultado}"

        # Caso de prueba 3: Patrón con caracteres especiales
        resultado = buscar_expresion_regular("¡Hola, ¿cómo estás?!", r"¡.*?!")
        assert resultado == True, f"Fallo en el caso de prueba 3. Se esperaba True, pero se obtuvo {resultado}"

        # Caso de prueba 4: Patrón que coincide al principio
        resultado = buscar_expresion_regular("12345", r"\d+")
        assert resultado == True, f"Fallo en el caso de prueba 4. Se esperaba True, pero se obtuvo {resultado}"

        # Caso de prueba 5: Cadena vacía con patrón vacío
        resultado = buscar_expresion_regular("", r"")
        assert resultado == True, f"Fallo en el caso de prueba 5. Se esperaba True, pero se obtuvo {resultado}"

        print("Todos los casos de prueba han pasado con éxito.")
