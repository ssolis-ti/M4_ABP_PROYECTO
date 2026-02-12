import unittest
from src.cliente import Cliente
from src.exceptions import DatosInvalidosError

class TestRUTValidation(unittest.TestCase):
    def test_rut_valido(self):
        # RUT limpio
        self.assertEqual(Cliente.validar_rut("12345678K"), "12345678K")
        # RUT con minusculas (debe convertir a mayusculas)
        self.assertEqual(Cliente.validar_rut("12345678k"), "12345678K")

    def test_rut_invalido_puntos(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente.validar_rut("12.345.678-K")

    def test_rut_invalido_guion(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente.validar_rut("12345678-K")

    def test_rut_invalido_caracteres(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente.validar_rut("12345678$")

if __name__ == '__main__':
    unittest.main()
