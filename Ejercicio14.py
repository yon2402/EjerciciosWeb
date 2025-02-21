import random

def generar_vector():
    return [random.randint(0, 99) for _ in range(10)]

def main():
    ROWS, COLS = 3, 10

    vector1 = generar_vector()
    vector2 = generar_vector()
    vector3 = generar_vector()

    matrix = [vector1, vector2, vector3]

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Vector 3:", vector3)

    print("\nMatriz generada:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()