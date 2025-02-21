def main():
    # Solicita al usuario que ingrese el tamaño del vector y lo convierte a entero
    size = int(input("Digite el tamaño del vector (+0): "))
    
    
    # Crea una lista vacía para almacenar los números
    numbers = []
    
    # Itera desde 0 hasta size-1 para solicitar cada elemento del vector
    for i in range(size):
        # Solicita al usuario el valor del elemento i+1 y lo convierte a entero
        number = int(input(f"Elemento {i + 1}: "))
        # Agrega el número ingresado a la lista
        numbers.append(number)
    
    # Calcula el número mayor usando la función max() de Python
    max_value = max(numbers)
    # Calcula el número menor usando la función min() de Python
    min_value = min(numbers)
    
    # Imprime el vector completo de números ingresados
    print("Vector ingresado:", numbers)
    # Imprime el número mayor encontrado en el vector
    print("Número mayor:", max_value)
    # Imprime el número menor encontrado en el vector
    print("Número menor:", min_value)

# Verifica si el script se está ejecutando directamente y llama a la función main
if __name__ == "__main__":
    main()
