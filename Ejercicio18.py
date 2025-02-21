import random  # Importa el módulo random para generar números aleatorios

def generate_random_numbers(amount, min_val, max_val):
    """Genera una lista de números aleatorios en un rango dado."""
    return [random.randint(min_val, max_val) for _ in range(amount)]
    # Crea una lista de tamaño 'amount' con valores aleatorios entre 'min_val' y 'max_val'.

def filter_range(min_val, max_val, numbers):
    """Filtra los números que están dentro del rango especificado [min_val, max_val]."""
    return [num for num in numbers if min_val <= num <= max_val]
    # Recorre la lista 'numbers' y guarda solo los valores dentro del rango [min_val, max_val].

def main():
    # Solicita al usuario la cantidad de números a generar y los límites del rango
    amount = int(input("Ingrese la cantidad de números aleatorios: "))
    min_val = int(input("Ingrese el valor mínimo del rango: "))
    max_val = int(input("Ingrese el valor máximo del rango: "))

    # Verifica que el mínimo no sea mayor que el máximo
    if min_val > max_val:
        print("Error: El valor mínimo no puede ser mayor que el máximo.")
        return  # Sale de la función si los valores no son válidos

    # Genera la lista de números aleatorios en el rango dado
    numbers = generate_random_numbers(amount, min_val, max_val)
    print(f"Lista generada: {numbers}")  # Muestra la lista generada

    # Filtra los números dentro del rango (en este caso, la lista será igual a la original)
    filtered_numbers = filter_range(min_val, max_val, numbers)
    print(f"Números en el rango [{min_val}, {max_val}]: {filtered_numbers}")

# Ejecuta la función main solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()

