class GICException(Exception):
    """
    excepcion base para nuestro sistema. 
    porque necesitamos diferenciar nuestros errores de los de python.
    para que el control de errores sea mas especifico.
    """
    pass

class ClienteExistenteError(GICException):
    """
    se lanza cuando intentamos meter a un cliente que ya existe.
    porque no queremos duplicados.
    para mantener la base de datos limpia.
    """
    pass

class ClienteNoEncontradoError(GICException):
    """
    se usa cuando buscamos un cliente y no aparece.
    porque no podemos borrar o editar a quien no existe.
    para avisar al usuario del error.
    """
    pass

class DatosInvalidosError(GICException):
    """
    error para cuando los datos estan mal formados.
    porque necesitamos info confiable.
    para evitar guardar basura en el sistema.
    """
    pass

class PersistenciaError(GICException):
    """
    si falla algo al guardar o leer el archivo json.
    porque el disco puede fallar o el archivo corromperse.
    para manejar problemas de entrada/salida.
    """
    pass
