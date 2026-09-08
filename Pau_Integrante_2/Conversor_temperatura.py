"""
Programa: Conversor de Temperatura
Integrante: Integrante 2
Descripción: Solicita una temperatura en grados Celsius y la convierte a grados Fahrenheit.
Fórmula: Fahrenheit = (Celsius * 9 / 5) + 32
"""

def main():
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius:g} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()
    