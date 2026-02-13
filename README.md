# Gestor Inteligente de Clientes (GIC)

## Descripción del Proyecto

Este proyecto implementa un sistema para gestionar clientes de una empresa (SolutionTech). Permite crear, listar, buscar y eliminar clientes, diferenciando entre tipos (Regular, Premium, Corporativo).

El sistema guarda los datos automáticamente en un archivo JSON para que no se pierdan al cerrar el programa.
Se requiere el ingreso de RUT sin puntos ni guiones para identificar a los clientes.

## Cómo ejecutar

1. Asegúrate de tener Python instalado.
2. Abre una terminal en la carpeta `M4`.
3. Ejecuta el archivo principal:

   ```bash
   python src/main.py
   ```
o iniciar directamente desde el .bat (esta limpio revisen antes con notepad por seguridad)

## Estructura del Proyecto

- `src/`: Contiene todo el código fuente.
  - `cliente.py`: Clase base (plantilla).
  - `tipos_clientes.py`: Los diferentes tipos de clientes.
  - `gestor.py`: Quien manda y organiza los datos.
  - `exceptions.py`: Errores personalizados.
  - `main.py`: El menú que ve el usuario.
- `data/`: Donde se guardan los datos (`clientes.json`).
- `tests/`: Pruebas automáticas.

## Tecnologías

- Python 3
- POO (Herencia, Polimorfismo, Encapsulamiento)
- JSON (para persistencia)


## Documentación Adicional

- [Conceptos de POO](docs/conceptos_poo.md): Explicación teórica solicitada.
- [Matriz de Entregables](entregables.md): Lista de requisitos cumplidos.
- [Diagrama UML (PDF)](docs/uml_diagram.pdf): Estructura visual en PDF.
- [Diagrama UML (Código)](docs/uml_diagram.mermaid): Código fuente del diagrama.

---
*Proyecto realizado para el Módulo 4.*
