import unittest
from  calculations import sumar_numeros

class calculation_test(unittest.TestCase):
    def test_sumar_numeros(self):
        # Caso de prueba 1: Números positivos
        resultado = sumar_numeros(2, 3)
        assert resultado == 5, f"Fallo en el caso de prueba 1. Se esperaba 5, pero se obtuvo {resultado}"

        # Caso de prueba 2: Números negativos
        resultado = sumar_numeros(-5, -7)
        assert resultado == -12, f"Fallo en el caso de prueba 2. Se esperaba -12, pero se obtuvo {resultado}"

        # Caso de prueba 3: Números mixtos
        resultado = sumar_numeros(10, -3)
        assert resultado == 7, f"Fallo en el caso de prueba 3. Se esperaba 7, pero se obtuvo {resultado}"

        # Caso de prueba 4: Números decimales
        resultado = sumar_numeros(2.5, 1.5)
        assert resultado == 4.0, f"Fallo en el caso de prueba 4. Se esperaba 4.0, pero se obtuvo {resultado}"

        # Caso de prueba 5: Números grandes
        resultado = sumar_numeros(1000000, 2000000)
        assert resultado == 3000000, f"Fallo en el caso de prueba 5. Se esperaba 3000000, pero se obtuvo {resultado}"

        # Caso de prueba 6: Números de cero
        resultado = sumar_numeros(0, 0)
        assert resultado == 0, f"Fallo en el caso de prueba 6. Se esperaba 0, pero se obtuvo {resultado}"

        print("Todos los casos de prueba han pasado con éxito.")
