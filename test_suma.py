import unittest
from calculadora import (
    suma, resta, multiplicacion, division, potencia, raiz_cuadrada, logaritmo, seno, coseno, tangente
)

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 5), 15)
        self.assertEqual(multiplicacion(-1, 1), -1)
        self.assertEqual(multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-1, 1), -1)
        self.assertEqual(division(-1, -1), 1)
        self.assertEqual(division(5, 0), "Error: División por cero")

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(-1, 2), 1)
        self.assertEqual(potencia(-1, 3), -1)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(4), 2)
        self.assertEqual(raiz_cuadrada(9), 3)
        self.assertEqual(raiz_cuadrada(-1), "Error: Raíz cuadrada de un número negativo")

    def test_logaritmo(self):
        self.assertEqual(logaritmo(100), 2)
        self.assertEqual(logaritmo(100, 10), 2)
        self.assertEqual(logaritmo(8, 2), 3)
        self.assertEqual(logaritmo(-1), "Error: Logaritmo de un número no positivo")

    def test_seno(self):
        self.assertAlmostEqual(seno(0), 0)
        self.assertAlmostEqual(seno(90), 1)
        self.assertAlmostEqual(seno(180), 0)

    def test_coseno(self):
        self.assertAlmostEqual(coseno(0), 1)
        self.assertAlmostEqual(coseno(90), 0)
        self.assertAlmostEqual(coseno(180), -1)

    def test_tangente(self):
        self.assertAlmostEqual(tangente(0), 0)
        self.assertAlmostEqual(tangente(45), 1)
        self.assertAlmostEqual(tangente(135), -1)

if __name__ == '__main__':
    unittest.main()
