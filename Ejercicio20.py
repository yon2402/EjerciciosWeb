def main():
    amount = int(input("Ingrese la cantidad de números en la lista: "))

    print(f"Ingrese los {amount} números:")
    numbers = [int(input()) for _ in range(amount)]

    argument = int(input("Indique el argumento: "))

    result = [num for num in numbers if num <= argument]

    print(f"Matriz original: {numbers}")
    
    print(f"Matriz filtrada: {result}")

if __name__ == "__main__":
    main()