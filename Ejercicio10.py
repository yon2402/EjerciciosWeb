def main():
    # Se crea una lista vacía para almacenar los 15 valores ingresados por el usuario.
    numbers = []
    
    # Se itera 15 veces, ya que se requieren 15 elementos.
    for i in range(15):
        # Solicita al usuario ingresar el valor del elemento (i+1) y lo convierte a entero.
        number = int(input(f"Elemento {i + 1}: "))
        # Agrega el valor ingresado a la lista 'numbers'.
        numbers.append(number)
    
    # Crea una nueva lista 'reversed_numbers' que contiene los elementos de 'numbers' en orden inverso.
    # En Python, se puede lograr utilizando slicing con [::-1].
    reversed_numbers = numbers[::-1]
    
    # Imprime la lista original de valores.
    print("Valores originales:", numbers)
    # Imprime la lista con los valores en orden inverso.
    print("Valores en orden inverso:", reversed_numbers)

# Verifica si el script se está ejecutando directamente y, en ese caso, llama a la función 'main'.
if __name__ == "__main__":
    main()
