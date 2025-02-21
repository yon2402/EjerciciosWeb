def main():
    # Crear una lista vacía para almacenar los 16 números que ingrese el usuario
    numbers = []
    
    # Iterar 16 veces para solicitar cada uno de los 16 números
    for i in range(16):
        # Solicitar al usuario que ingrese el número correspondiente (se muestra el índice + 1 para mayor claridad)
        number = int(input(f"Ingrese el elemento {i + 1} : "))
        # Agregar el número ingresado a la lista 'numbers'
        numbers.append(number)
    
    # Dividir la lista 'numbers' en dos mitades:
    # 'first_half' contendrá los primeros 8 elementos (índices 0 a 7)
    first_half = numbers[:8]
    # 'second_half' contendrá los 8 elementos restantes (índices 8 a 15)
    second_half = numbers[8:]
    
    # Imprimir la lista completa de números ingresados
    print("Lista completa:", numbers)
    # Imprimir la primera mitad de la lista
    print("Primera mitad:", first_half)
    # Imprimir la segunda mitad de la lista
    print("Segunda mitad:", second_half)

# Verificar si el script se está ejecutando directamente y, de ser así, llamar a la función main()
if __name__ == "__main__":
    main()
