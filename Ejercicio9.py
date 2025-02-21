def main():
    size = int(input("Digite el tamaño del vector (+0): "))
    
    numbers = []
    
    for i in range(size):
        number = int(input(f"Elemento {i + 1}: "))
        numbers.append(number)
    
    max_value = max(numbers)
    min_value = min(numbers)
    
    print("Vector ingresado:", numbers)
    print("Número mayor:", max_value)
    print("Número menor:", min_value)

if __name__ == "__main__":
    main()