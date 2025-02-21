def main():
    numbers = []
    
    for i in range(15):
        number = int(input(f"Elemento {i + 1}: "))
        numbers.append(number)
    
    reversed_numbers = numbers[::-1]
    
    print("Valores originales:", numbers)
    print("Valores en orden inverso:", reversed_numbers)

if __name__ == "__main__":
    main()