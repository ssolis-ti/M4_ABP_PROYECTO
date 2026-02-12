from abc import ABC, abstractmethod
import re
from src.exceptions import DatosInvalidosError

class Cliente(ABC):
    """
    clase 'padre' (abstracta) para todos los clientes.
    porque necesitamos una plantilla base comun.
    para obligar a que todos los clientes tengan nombre, email y cif.
    """

    def __init__(self, nombre: str, email: str, rut: str):
        # inicializamos los datos basicos. porque el objeto necesita estado inicial. para usarlo despues.
        self._nombre = nombre
        # validamos el email antes de guardarlo. porque si esta mal no nos sirve. para asegurar calidad de datos.
        self._email = self.validar_email(email)
        self._rut = self.validar_rut(rut)

    # --- propiedades (getters y setters) ---
    # usamos esto para proteger los datos. porque no queremos accesos directos. para controlar como se modifican.

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        # si cambian el email, lo volvemos a validar. porque el nuevo valor podria estar mal. para mantener la integridad.
        self._email = self.validar_email(valor)

    @property
    def rut(self):
        return self._rut

    @staticmethod
    def validar_email(email: str) -> str:
        """
        revisa que el email tenga formato correcto.
        porque un email malo no sirve para contactar.
        para filtrar entradas incorrectas del usuario.
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, email):
            # si no encaja con el patron, lanzamos error. porque no cumple la regla. para detener el proceso.
            raise DatosInvalidosError(f"el email '{email}' no es valido.")
        return email

    @staticmethod
    def validar_rut(rut: str) -> str:
        """
        revisa que el rut no tenga puntos ni guiones y sea alfanumerico.
        porque el sistema lo requiere limpio.
        para evitar formatos inconsistentes.
        """
        if not rut.isalnum():
             raise DatosInvalidosError(f"el RUT '{rut}' no es valido. Debe ser sin puntos ni guion y solo numeros y K.")
        return rut.upper() # guardamos en mayusculas por si acaso.

    def __str__(self):
        # define como se ve el cliente en texto. porque ayuda a leerlo en consola. para mostrar info rapida.
        return f"Cliente: {self.nombre} | RUT: {self.rut} | Email: {self.email}"

    def __eq__(self, other):
        # compara dos clientes por id. porque el objeto en memoria es distinto pero el cliente es el mismo. para evitar duplicados logicos.
        if not isinstance(other, Cliente):
            return False
        return self.rut == other.rut

    def __repr__(self):
        """
        representacion tecnica del objeto.
        porque es util para los programadores.
        para ver detalles en el debugger o logs.
        """
        return f"<{self.__class__.__name__}(rut='{self.rut}', email='{self.email}')>"

    @abstractmethod
    def to_dict(self) -> dict:
        """
        metodo abstracto para convertir a diccionario.
        porque json no entiende de objetos python.
        para poder guardarlo en un archivo de texto.
        obliga a las clases hijas a implementarlo. porque si no, no pueden ser instanciadas. para contrato estricto.
        """
        pass
