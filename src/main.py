from src.gestor import GestorClientes
from src.cliente import Cliente
from src.tipos_clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from src.exceptions import GICException

def leer_campo(mensaje: str, validar_func=None) -> str:
    """
    Lee un campo de texto y valida que no se vacio.
    Opcionalmente aplica una validacion extra.
    """
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: Este campo no puede estar vacío.")
            continue
        
        if validar_func:
            try:
                # la funcion validadora debe lanzar error o devolver False si falla
                if not validar_func(valor):
                     print("Error: Entrada inválida.")
                     continue
            except Exception as e:
                print(f"Error: {e}")
                continue
                
        return valor

def leer_float(mensaje: str) -> float:
    """
    funcion de ayuda para leer numeros.
    porque el usuario puede escribir letras.
    para que el programa no explote por error de tipo.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número válido (ej. 10.5).")

def main():
    print("=== Gestor Inteligente de Clientes (GIC) ===")
    
    # creamos el gestor. porque necesitamos iniciar la logica. para cargar los datos previos del json.
    gestor = GestorClientes()

    while True:
        # menu principal. bucle infinito. porque queremos seguir operando. para que el usuario elija salir.
        print("\n--- Opciones ---")
        print("1. Agregar Cliente Regular")
        print("2. Agregar Cliente Premium")
        print("3. Agregar Cliente Corporativo")
        print("4. Buscar Cliente")
        print("5. Eliminar Cliente")
        print("6. Listar Clientes")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        try:
            # opcion 1: cliente regular. porque es el basico. para gente normal.
            if opcion == '1':
                print("\n[Nuevo Cliente Regular]")
                nombre = leer_campo("Nombre: ")
                email = leer_campo("Email: ", Cliente.validar_email)
                rut = leer_campo("RUT (sin puntos ni guion): ", Cliente.validar_rut)
                # usamos nuestra funcion segura. porque input devuelve str. para convertir a float.
                while True:
                    desc_input = leer_float("Descuento (0-100%): ")
                    if 0 <= desc_input <= 100:
                        desc = desc_input / 100.0
                        break
                    print("Error: El descuento debe estar entre 0 y 100.")
                c = ClienteRegular(nombre, email, rut, desc)
                gestor.agregar_cliente(c)
                print("Cliente Regular agregado con éxito.")

            # opcion 2: cliente premium. porque paga cuota. para gente vip.
            elif opcion == '2':
                print("\n[Nuevo Cliente Premium]")
                nombre = leer_campo("Nombre: ")
                email = leer_campo("Email: ", Cliente.validar_email)
                rut = leer_campo("RUT (sin puntos ni guion): ", Cliente.validar_rut)
                cuota = leer_float("Cuota Mensual: ")
                c = ClientePremium(nombre, email, rut, cuota)
                gestor.agregar_cliente(c)
                print("Cliente Premium agregado con éxito.")

            # opcion 3: corporativo. porque es empresa. para gestionar negocios.
            elif opcion == '3':
                print("\n[Nuevo Cliente Corporativo]")
                nombre = leer_campo("Nombre: ")
                email = leer_campo("Email: ", Cliente.validar_email)
                rut = leer_campo("RUT (sin puntos ni guion): ", Cliente.validar_rut)
                contacto = leer_campo("Contacto Empresa: ")
                c = ClienteCorporativo(nombre, email, rut, contacto)
                gestor.agregar_cliente(c)
                print("Cliente Corporativo agregado con éxito.")

            # opcion 4: buscar. porque necesitamos ver datos. para encontrar a alguien por su id.
            elif opcion == '4':
                rut = leer_campo("Ingrese RUT a buscar: ", Cliente.validar_rut)
                cliente = gestor.buscar_cliente(rut)
                if cliente:
                    # al imprimir cliente se llama a str. porque asi lo definimos. para ver sus datos bonitos.
                    print(f"Encontrado: {cliente}")
                else:
                    print("Cliente no encontrado.")

            # opcion 5: borrar. porque ya no es cliente. para quitarlo de la lista.
            elif opcion == '5':
                rut = leer_campo("Ingrese RUT a eliminar: ", Cliente.validar_rut)
                gestor.eliminar_cliente(rut)
                print("Cliente eliminado.")

            # opcion 6: ver todos. porque queremos un resumen. para listar lo que hay en memoria.
            elif opcion == '6':
                print("\n--- Lista de Clientes ---")
                if not gestor.clientes:
                    print("No hay clientes registrados.")
                for c in gestor.clientes:
                    print(c)

            # opcion 7: salir. porque terminamos. para romper el bucle y cerrar el programa.
            elif opcion == '7':
                print("Saliendo del sistema...")
                break 
            
            else:
                print("Opción no válida.")

        # capturamos errores controlados. porque definimos excepciones propias. para mensajes claros.
        except GICException as e:
            print(f"ERROR DEL SISTEMA: {e}")
        # capturamos errores inesperados. porque algo puede fallar. para que no crashee feo.
        except Exception as e:
            print(f"ERROR INESPERADO: {e}")

if __name__ == "__main__":
    # punto de entrada. porque python necesita saber donde empezar. para ejecutar el main.
    main()
