def main():
    # Se crea una lista vacía para almacenar los 20 números que ingresará el usuario
    numbers = []
    
    # Se itera 20 veces para leer cada número
    for i in range(20):
        # Se solicita al usuario que ingrese el número correspondiente (se muestra el índice + 1)
        number = int(input(f"Ingrese el elemento {i + 1}: "))
        # Se agrega el número ingresado a la lista
        numbers.append(number)
    
    # Se utiliza la función max() para encontrar el mayor valor en la lista
    max_value = max(numbers)
    
    # Se obtiene la posición (índice) del primer elemento que coincida con el valor máximo
    max_position = numbers.index(max_value)
    
    # Se imprime la lista completa de números ingresados
    print("Numeros ingresados:", numbers)
    # Se imprime el mayor número y la posición en la que se encuentra dentro de la lista
    print(f"Numero mayor: {max_value} en la posicion: {max_position}")

# Se verifica si el script se está ejecutando directamente y, de ser así, se llama a la función main()
if __name__ == "__main__":
    main()
