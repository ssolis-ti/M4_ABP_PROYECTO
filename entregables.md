# Matriz de Entregables - Proyecto GIC

Este documento vincula los requisitos solicitados en el PDF con su implementación en el código.

## 1. Paradigma de Orientación a Objetos

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| Documento explicativo sobre POO | `docs/conceptos_poo.md` |
| Clase Cliente con atributos básicos | `src/cliente.py` (Clase `Cliente`) |
| Ejemplo de instanciación y métodos | `src/main.py` (Lógica de creación) y `tests/` |

## 2. Programación Orientada a Objetos en Python

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| Clases y métodos con encapsulación | `src/cliente.py` (Uso de `_atributo` y `@property`) |
| Validaciones en atributos | `src/cliente.py` (Método `validar_email`) |
| Métodos especiales (`__str__`, `__eq__`) | `src/cliente.py` (Líneas 50-60) |

## 3. Diagramas de Clase

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| Modelo UML detallado | `docs/uml_diagram.mermaid` |
| Relaciones (Herencia, Composición) | Visible en diagrama y código (`Gestor` tiene lista de `Cliente`) |

## 4. Herencia y Polimorfismo

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| Subclases de tipos de clientes | `src/tipos_clientes.py` (`Regular`, `Premium`, `Corporativo`) |
| Métodos sobrescritos/polimórficos | `to_dict()` y `__str__` en cada subclase |
| Uso de `super()` | `src/tipos_clientes.py` (En cada `__init__`) |

## 5. Manejo de Errores y Excepciones

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| Excepciones personalizadas | `src/exceptions.py` |
| Validación de datos (Interfaz) | `src/main.py` (Función `leer_float`, bloques `try-except`) |
| Logs de errores | `src/gestor.py` (Librería `logging` escribiendo a `app.log`) |

## 6. Persistencia y Pruebas

| Requisito | Implementación / Archivo |
|-----------|--------------------------|
| JSON para almacenamiento | `src/gestor.py` (Métodos `guardar_datos` / `cargar_datos`) |
| Pruebas Unitarias | `tests/test_gestion_clientes.py` (Cobertura completa) |

---
**Estado del Proyecto:** 100% Completado y Verificado.
