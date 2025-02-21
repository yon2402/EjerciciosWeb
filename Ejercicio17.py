import random  # Importa el módulo random para generar números aleatorios

def generate_list(size):
    """Genera una lista de números aleatorios entre 1 y 100."""
    return [random.randint(1, 100) for _ in range(size)]
    # Crea una lista de tamaño 'size' con valores aleatorios entre 1 y 100.

def divide_list_by_two(lst):
    """Filtra los números pares y los divide por 2."""
    return [n / 2 for n in lst if n % 2 == 0]
    # Recorre la lista 'lst' y selecciona solo los números pares (n % 2 == 0).
    # Luego, divide cada número par por 2 y lo almacena en una nueva lista.

def main():
    size = int(input("Ingrese el tamaño de la lista: "))  # Pide al usuario el tamaño de la lista

    numbers = generate_list(size)  # Genera la lista con números aleatorios
    result = divide_list_by_two(numbers)  # Filtra los pares y los divide por 2

    print("Lista original:", numbers)  # Muestra la lista generada
    print("\nLista transformada:", result)  # Muestra la lista con los números pares divididos por 2

# Ejecuta la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
