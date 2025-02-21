def main():
    amount = int(input("Ingrese la cantidad de números en la lista: "))

    print(f"Ingrese los {amount} números:")
    numbers = [int(input()) for _ in range(amount)]

    positives = sum(1 for num in numbers if num >= 0)

    print(f"Lista original: {numbers}")
    
    print(f"Cantidad de números positivos (incluyendo el 0): {positives}")

if __name__ == "__main__":
    main()