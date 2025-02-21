def main():
    numbers = []
    
    for i in range(20):
        number = int(input(f"Ingrese el elemento {i + 1}: "))
        numbers.append(number)
    
    max_value = max(numbers)
    max_position = numbers.index(max_value)
    
    print("Numeros ingresados:", numbers)
    print(f"Numero mayor: {max_value} en la posicion: {max_position}")

if __name__ == "__main__":
    main()