import json
import logging
from typing import List, Optional
from src.cliente import Cliente
from src.tipos_clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from src.exceptions import ClienteExistenteError, ClienteNoEncontradoError, PersistenciaError

# configuramos el logging. porque necesitamos ver que pasa. para diagnositcar errores despues.
# configuramos el logging. porque necesitamos ver que pasa. para diagnositcar errores despues.
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='[%(levelname)s] %(funcName)s: %(message)s',
    filemode='w' # sobrescribe cada vez. porque queremos limpiar log en cada ejecucion como pidio el usuario.
)

class GestorClientes:
    """
    el cerebro de la operacion.
    porque necesitamos alguien que administre la lista.
    para centralizar agregar, borrar y guardar.
    """
    
    def __init__(self, archivo_path: str = 'data/clientes.json'):
        self.archivo_path = archivo_path
        self.clientes: List[Cliente] = [] # lista en memoria. porque es mas rapido. para operar al instante.
        self.cargar_datos() # leemos al arrancar. porque queremos recuperar sesiones previas. para no perder datos.

    def agregar_cliente(self, cliente: Cliente):
        """añade un cliente nuevo. porque necesitamos crecer la base. para guardarlo en sistema."""
        # verificamos duplicados. porque el id debe ser unico. para evitar confusiones.
        if any(c.rut == cliente.rut for c in self.clientes):
            raise ClienteExistenteError(f"el cliente con RUT {cliente.rut} ya existe.")
        
        self.clientes.append(cliente)
        logging.debug(f"cliente en memoria antes de guardar: {cliente}")
        logging.info(f"cliente agregado: {cliente.rut}") # dejamos rastro. porque es bueno auditar. para seguridad.
        self.guardar_datos() # guardamos ya. porque si se luz se pierde. para persistencia inmediata.

    def eliminar_cliente(self, rut: str):
        """borra un cliente. porque ya no es cliente. para limpiar la base."""
        cliente = self.buscar_cliente(rut)
        if not cliente:
            raise ClienteNoEncontradoError(f"no se encontro cliente con RUT {rut}")
        
        self.clientes.remove(cliente)
        logging.info(f"cliente eliminado: {rut}")
        self.guardar_datos()

    def buscar_cliente(self, rut: str) -> Optional[Cliente]:
        """busca un cliente. porque a veces necesitamos ver sus datos. para encontrarlo por su id unico."""
        logging.debug(f"buscando rut: {rut}")
        # next nos da el primero. porque solo deberia haber uno. para ser eficientes.
        return next((c for c in self.clientes if c.rut == rut), None)

    def guardar_datos(self):
        """vuelca memoria a disco. porque la ram es volatil. para persistencia permanente."""
        try:
            # pasamos a dict. porque json solo entiende texto estructurado. para poder guardarlo.
            data = [c.to_dict() for c in self.clientes]
            with open(self.archivo_path, 'w', encoding='utf-8') as f:
                # dump escribe el archivo. indent es para que se lea bien. para formato bonito.
                # ensure_ascii=False permite tildes y ñ. porque hablamos español. para que no salgan codigos raros.
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            logging.error(f"error guardando datos: {e}")
            raise PersistenciaError(f"no se pudieron guardar los datos: {e}")

    def cargar_datos(self):
        """lee el json y reconstruye. porque al iniciar esta todo vacio. para restaurar el estado anterior."""
        try:
            import os
            if not os.path.exists(self.archivo_path):
                return # si no hay archivo no hacemos nada. porque es la primera vez. para evitar errores.

            with open(self.archivo_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                logging.debug(f"datos crudos cargados: {len(data)} items")

            self.clientes = []
            for item in data:
                # metemos parche para compatibilidad. porque antes usabamos cif_nif. para que no explote con datos viejos.
                if 'cif_nif' in item:
                    item['rut'] = item.pop('cif_nif')

                # sacamos el tipo. porque necesitamos saber la clase. para el polimorfismo.
                tipo = item.pop('type', 'Regular')
                if tipo == 'Regular':
                    # **item desempaqueta datos. porque coinciden con los argumentos. para instanciar rapido.
                    self.clientes.append(ClienteRegular(**item))
                elif tipo == 'Premium':
                    self.clientes.append(ClientePremium(**item))
                elif tipo == 'Corporativo':
                    self.clientes.append(ClienteCorporativo(**item))
                else:
                    logging.warning(f"tipo desconocido: {tipo}")

        except Exception as e:
            logging.error(f"error cargando datos: {e}")
            # solo avisamos. porque si falla la carga podemos seguir vacios. para que la app no muera.
            print(f"advertencia: no se pudieron cargar los datos previos ({e})")
