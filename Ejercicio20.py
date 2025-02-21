def main():
    # Solicita al usuario la cantidad de números en la lista
    amount = int(input("Ingrese la cantidad de números en la lista: "))

    print(f"Ingrese los {amount} números:")
    # Crea una lista con los números ingresados por el usuario
    numbers = [int(input()) for _ in range(amount)]

    # Solicita al usuario un valor de referencia (argumento)
    argument = int(input("Indique el argumento: "))

    # Filtra los números que sean menores o iguales al argumento
    result = [num for num in numbers if num <= argument]

    # Muestra la lista original ingresada por el usuario
    print(f"Matriz original: {numbers}")
    
    # Muestra la lista filtrada con los valores menores o iguales al argumento
    print(f"Matriz filtrada: {result}")

# Ejecuta la función main solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()
