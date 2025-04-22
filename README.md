![product_validation_system_banner2](https://github.com/user-attachments/assets/c8f3e51e-288e-4556-8aff-53e6285b231f)

# 🛒 Sistema de Validación de Productos

### 📘 English version  
[Click here to see the README in English](./README_EN.md)

## 📌 Descripción del Proyecto

Este ejercicio fue desarrollado como parte del **Módulo 1 – Semana 1 del entrenamiento**. El objetivo principal es construir una aplicación que permita **calcular el costo total de una compra** en una tienda, validando correctamente los datos ingresados por el usuario y aplicando descuentos si corresponde.

---

## 🎯 Funcionalidades

- Solicita al usuario los siguientes datos:
  - Nombre del producto
  - Precio unitario (número positivo)
  - Cantidad de productos (número positivo)
  - Porcentaje de descuento (entre 0 y 100)
- Valida que los datos ingresados sean correctos y estén dentro de los rangos permitidos.
- Calcula:
  - El costo total sin descuento
  - El costo final con descuento aplicado (si corresponde)
- Muestra el resultado con dos decimales y de forma legible.

---

## 🧠 Lógica Implementada

- Se implementaron dos funciones específicas para validar entradas numéricas:
  - `validar_numero_positivo(num)`
  - `validar_descuento(num)`
- La lógica principal calcula el total **multiplicando el precio por la cantidad** y luego aplica el **descuento**, si es mayor a 0.
- El resultado se muestra con formato monetario (dos decimales), junto con el nombre del producto.

---

## ✅ Validaciones Realizadas

Se probaron los siguientes escenarios:

1. Producto sin descuento
2. Producto con descuento del 100%
3. Descuento fuera del rango (rechazado)
4. Ingreso de letras o símbolos no válidos (rechazado)
5. Cantidad o precio igual a cero

Todos los casos se manejan correctamente sin generar errores de ejecución.

---

## 📁 Estructura del Código

- Código estructurado en funciones reutilizables
- Módulo principal organizado con comentarios para facilitar su comprensión
- Mensajes claros para la interacción con el usuario

---

## 🧩 Justificación Técnica

Se aplicaron funciones específicas para separar responsabilidades y garantizar **modularidad**, lo que facilita el mantenimiento y posibles extensiones del código. Además:

- Se usó `float()` en lugar de `int()` para permitir precios y cantidades con decimales, ajustándose mejor a un entorno real de ventas.
- Se incorporó manejo de errores con `try/except` para capturar entradas inválidas y evitar interrupciones en la ejecución.
- Se implementó **formateo de salida con dos decimales**, lo que mejora la presentación y comprensión del valor total.

Estas decisiones favorecen la **claridad, escalabilidad y calidad** del código, alineándose con buenas prácticas de desarrollo.

---

## 🚀 Mejoras Futuras

Algunas posibles mejoras para versiones posteriores:

- Implementar una interfaz gráfica (GUI) usando Tkinter o PyQt.
- Permitir el ingreso de múltiples productos en una misma sesión y mostrar el total acumulado.
- Guardar un historial de compras en un archivo externo (CSV o JSON).
- Validar que el nombre del producto no esté vacío o que tenga un formato específico.
- Internacionalizar el formato monetario (p. ej., usando separadores de miles o símbolo de moneda local).

---

## 💻 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema (versión recomendada: Python 3.8 o superior).
2. Clona el repositorio desde GitHub con el siguiente comando:

   ```bash
   git clone https://github.com/Sam-SSD/Products-Validation-System.git
   ```

3. Ingresa al directorio del proyecto:

   ```bash
   cd Products-Validation-System
   ```

4. Ejecuta el archivo principal con el siguiente comando:

   ```bash
   python validacion_de_productos.py
   ```

5. Sigue las instrucciones en pantalla para ingresar los datos solicitados.

---
