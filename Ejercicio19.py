def main():
    # Solicita al usuario la cantidad de números que tendrá la lista
    amount = int(input("Ingrese la cantidad de números en la lista: "))

    print(f"Ingrese los {amount} números:")
    # Crea una lista con los números ingresados por el usuario
    numbers = [int(input()) for _ in range(amount)]

    # Cuenta cuántos números son positivos (incluyendo el 0)
    positives = sum(1 for num in numbers if num >= 0)

    # Muestra la lista ingresada por el usuario
    print(f"Lista original: {numbers}")
    
    # Muestra la cantidad de números positivos en la lista
    print(f"Cantidad de números positivos (incluyendo el 0): {positives}")

# Ejecuta la función main solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()
