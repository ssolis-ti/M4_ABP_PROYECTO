import unittest
import os
import json
from src.cliente import Cliente
from src.tipos_clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from src.gestor import GestorClientes
from src.exceptions import ClienteExistenteError, ClienteNoEncontradoError, DatosInvalidosError

class TestGIC(unittest.TestCase):
    """
    clase de pruebas automaticas.
    porque probar a mano cansa y falla.
    para asegurar que el codigo siempre funcione.
    """
    
    def setUp(self):
        """
        se ejecuta antes de cada prueba.
        porque necesitamos un entorno limpio.
        para no mezclar datos de pruebas anteriores.
        """
        self.test_db = 'data/test_clientes.json'
        # creamos carpeta data si no existe. porque el gestor la necesita. para evitar error de ruta.
        os.makedirs('data', exist_ok=True)
        # borramos rastro previo. porque queremos empezar de cero. para fiabilidad.
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        # iniciamos gestor de prueba. porque no queremos tocar la base real. para aislar el test.
        self.gestor = GestorClientes(archivo_path=self.test_db)

    def tearDown(self):
        """
        se ejecuta despues de cada prueba.
        porque somos ordenados.
        para borrar la basura que generamos.
        """
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_creacion_cliente_regular(self):
        """probamos crear un cliente. porque es la base de todo. para ver si guarda los atributos."""
        c = ClienteRegular("Juan Perez", "juan@example.com", "12345678A", descuento=0.1)
        self.assertEqual(c.nombre, "Juan Perez") 
        self.assertEqual(c.email, "juan@example.com") 
        self.assertEqual(c.descuento, 0.1) 

    def test_validacion_email_invalido(self):
        """probamos email falso. porque el usuario se equivoca. para asegurar que el sistema lo rechace."""
        # esperamos que lance error. porque el email esta mal. para validar la validacion.
        with self.assertRaises(DatosInvalidosError):
            ClienteRegular("Error", "email-invalido", "00000000T")

    def test_agregar_y_buscar_cliente(self):
        """probamos ciclo guardar-buscar. porque es el flujo principal. para asegurar que lo que entra sale igual."""
        c = ClientePremium("Ana Gomez", "ana@example.com", "87654321B", cuota_mensual=50.0)
        self.gestor.agregar_cliente(c)
        
        buscado = self.gestor.buscar_cliente("87654321B")
        self.assertIsNotNone(buscado) # no debe ser none. porque lo acabamos de guardar.
        self.assertEqual(buscado.nombre, "Ana Gomez")
        self.assertIsInstance(buscado, ClientePremium) # debe ser premium. porque asi lo creamos.

    def test_evitar_duplicados(self):
        """probamos duplicados. porque el id es unico. para que no haya dos clientes iguales."""
        c1 = ClienteCorporativo("Corp X", "contact@corpx.com", "B12345678", contacto_empresa="Manager")
        self.gestor.agregar_cliente(c1)
        
        c2 = ClienteCorporativo("Corp X Copy", "other@corpx.com", "B12345678", contacto_empresa="Other")
        # al intentar meter el segundo debe fallar. porque el id ya existe. para proteger la integridad.
        with self.assertRaises(ClienteExistenteError):
            self.gestor.agregar_cliente(c2)

    def test_persistencia_datos(self):
        """probamos reinicio. porque la app se cierra. para asegurar que los datos sobreviven al apagado."""
        c = ClienteRegular("Test Persistencia", "persistencia@test.com", "99999999P")
        self.gestor.agregar_cliente(c)
        
        # simulamos reinicio con nuevo gestor. porque la memoria se borra. para probar lectura de disco.
        nuevo_gestor = GestorClientes(archivo_path=self.test_db)
        recuperado = nuevo_gestor.buscar_cliente("99999999P")
        
        self.assertIsNotNone(recuperado) # debe estar ahi. porque se guardo en json.
        self.assertEqual(recuperado.email, "persistencia@test.com")

if __name__ == '__main__':
    unittest.main()
