from src.cliente import Cliente

class ClienteRegular(Cliente):
    """
    cliente normalito.
    porque es el tipo de cliente por defecto.
    para usuarios sin beneficios extra.
    """
    def __init__(self, nombre: str, email: str, rut: str, descuento: float = 0.0):
        # llamamos al constructor padre con super. porque heredamos su logica. para inicializar lo basico.
        super().__init__(nombre, email, rut)
        self.descuento = descuento

    def __str__(self):
        # reutilizamos el str del padre. porque ya tiene casi todo. para agregar solo el descuento.
        return super().__str__() + f" | Tipo: Regular | Descuento: {self.descuento*100}%"

    def to_dict(self) -> dict:
        # convertimos a diccionario. porque necesitamos serializar. para guardar en json incluyendo el tipo.
        return {
            "type": "Regular", # importante saber el tipo. porque al cargar necesitamos saber que clase crear. para reconstruir el objeto.
            "nombre": self.nombre,
            "email": self.email,
            "rut": self.rut,
            "descuento": self.descuento
        }

class ClientePremium(Cliente):
    """
    cliente vip.
    porque pagan mas.
    para darles trato especial y cobrar cuota.
    """
    def __init__(self, nombre: str, email: str, rut: str, cuota_mensual: float = 0.0):
        super().__init__(nombre, email, rut)
        self.cuota_mensual = cuota_mensual

    def __str__(self):
        return super().__str__() + f" | Tipo: Premium | Cuota: ${self.cuota_mensual:.2f}"

    def to_dict(self) -> dict:
        return {
            "type": "Premium",
            "nombre": self.nombre,
            "email": self.email,
            "rut": self.rut,
            "cuota_mensual": self.cuota_mensual
        }

class ClienteCorporativo(Cliente):
    """
    cliente de empresa.
    porque las empresas tienen contacto especifico.
    para gestionar cuentas coorporativas.
    """
    def __init__(self, nombre: str, email: str, rut: str, contacto_empresa: str = ""):
        super().__init__(nombre, email, rut)
        self.contacto_empresa = contacto_empresa

    def __str__(self):
        return super().__str__() + f" | Tipo: Corporativo | Contacto: {self.contacto_empresa}"

    def to_dict(self) -> dict:
        return {
            "type": "Corporativo",
            "nombre": self.nombre,
            "email": self.email,
            "rut": self.rut,
            "contacto_empresa": self.contacto_empresa
        }
