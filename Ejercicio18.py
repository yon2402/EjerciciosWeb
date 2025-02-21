import random  

def generate_random_numbers(amount, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(amount)]

def filter_range(min_val, max_val, numbers):
    return [num for num in numbers if min_val <= num <= max_val]

def main():
    amount = int(input("Ingrese la cantidad de números aleatorios: "))
    min_val = int(input("Ingrese el valor mínimo del rango: "))
    max_val = int(input("Ingrese el valor máximo del rango: "))

    if min_val > max_val:
        print("Error: El valor mínimo no puede ser mayor que el máximo.")
        return  

    numbers = generate_random_numbers(amount, min_val, max_val)
    print(f"Lista generada: {numbers}")

    filtered_numbers = filter_range(min_val, max_val, numbers)
    print(f"Números en el rango [{min_val}, {max_val}]: {filtered_numbers}")

if __name__ == "__main__":
    main()