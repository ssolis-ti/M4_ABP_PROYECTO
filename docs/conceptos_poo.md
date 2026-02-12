# Paradigma de Orientación a Objetos (POO)

## 1. Introducción

La Programación Orientada a Objetos (POO) es un modelo de programación que organiza el diseño de software alrededor de datos (objetos) en lugar de funciones y lógica. En este paradigma, los objetos son instancias de clases, que actúan como plantillas.

## 2. Importancia en Sistemas Escalables

En el contexto de **SolutionTech** y su *Gestor Inteligente de Clientes (GIC)*, la POO es fundamental por las siguientes razones:

* **Modularidad:** Permite dividir el sistema en partes independientes (`Cliente`, `Gestor`). Si algo falla en `ClienteRegular`, no afecta al resto del sistema.
* **Reutilización:** Gracias a la herencia, escribimos la lógica común una sola vez en la clase padre `Cliente` y la reutilizamos en todas las subclases.
* **Mantenibilidad:** Es más fácil entender y corregir código cuando simula objetos del mundo real (un "Cliente" que tiene "Nombre" y "Email").

## 3. Pilares de la POO en este Proyecto

### A. Encapsulamiento

Ocultamos los detalles internos y protegemos los datos.

* *En nuestro código:* Usamos atributos protegidos como `_email` y propiedades (`@property`) para que nadie pueda asignar un email inválido directamente.

### B. Herencia

Creamos nuevas clases basadas en clases existentes.

* *En nuestro código:* `ClienteRegular`, `ClientePremium` y `ClienteCorporativo` heredan de `Cliente`. Tienen todo lo que tiene un cliente, más sus propias características.

### C. Polimorfismo

Diferentes clases pueden responder al mismo método de manera distinta.

* *En nuestro código:* Todas las clases tienen el método `to_dict()`, pero cada una lo implementa diferente para guardar sus datos específicos (como el `descuento` o la `cuota_mensual`).

### D. Abstracción

Definimos qué hace un objeto sin preocuparnos de cómo.

* *En nuestro código:* La clase `Cliente` es abstracta (`ABC`). Define que todo cliente debe tener un método `to_dict()`, pero no dice cómo debe ser; obliga a sus hijos a definirlo.

---
*Documento generado para el cumplimiento del Entregable 1 del Proyecto Módulo 4.*
