def main():
    numbers = []
    
    for i in range(16):
        number = int(input(f"Ingrese el elemento {i + 1} : "))
        numbers.append(number)
    
    first_half = numbers[:8]
    second_half = numbers[8:]
    
    print("Lista completa:", numbers)
    print("Primera mitad:", first_half)
    print("Segunda mitad:", second_half)

if __name__ == "__main__":
    main()