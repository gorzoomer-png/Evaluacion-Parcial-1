# Programa: Calculadora de Descuento
# Autor: Integrante 1

def calcular_descuento():
    try:
        precio_original = float(input("Ingrese el precio del producto: $"))
        porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))

        monto_descuento = precio_original * (porcentaje_descuento / 100)
        precio_final = precio_original - monto_descuento

        print("\n--- Resultado ---")
        print(f"Precio original: ${precio_original:.2f}")
        print(f"Descuento aplicado: ${monto_descuento:.2f}")
        print(f"Total a pagar: ${precio_final:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    calcular_descuento()