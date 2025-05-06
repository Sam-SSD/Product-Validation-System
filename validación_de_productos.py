# Sistema de validación de productos

def validar_nombre_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre or nombre.isnumeric():
            print("Nombre inválido. Por favor, ingrese un nombre válido.")
        else:
            return nombre


def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número válido.")


def validar_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número entero mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número entero válido.")


def validar_descuento(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return 0.0
        try:
            descuento = float(entrada)
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingrese un número válido entre 0 y 100.")


# Módulo principal
print("---------- Bienvenido al sistema de validación de productos ----------")

nombre_producto = validar_nombre_producto()
precio_unitario = validar_numero_positivo("Ingrese el precio unitario del producto: ")
cantidad = validar_entero_positivo("Ingrese la cantidad de producto a comprar: ")

# Preguntar si desea aplicar descuento
respuesta = input("¿Desea aplicar un descuento? (sí/no): ").strip().lower()
if respuesta in ["sí", "si", "s"]:
    descuento = validar_descuento("Ingrese el porcentaje de descuento (0-100, Enter = 0): ")
else:
    descuento = 0.0

# Cálculo del costo total
costo_total = precio_unitario * cantidad
if descuento > 0:
    costo_total *= (1 - descuento / 100)
    mensaje_descuento = "con descuento"
else:
    mensaje_descuento = "sin descuento"

# Mostrar resultado con separador de miles y estado del descuento
print(f"\nEl costo total de la compra de {nombre_producto} ({mensaje_descuento}) es: ${costo_total:,.2f}")
print("---------------------------------------------------------------------")
