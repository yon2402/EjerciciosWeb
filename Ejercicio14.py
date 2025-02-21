import random

def generar_vector():
    """Genera un vector de 10 elementos con valores aleatorios entre 0 y 99."""
    return [random.randint(0, 99) for _ in range(10)]

def main():
    # Definir dimensiones de la matriz
    ROWS, COLS = 3, 10

    # Generar los tres vectores aleatorios
    vector1 = generar_vector()
    vector2 = generar_vector()
    vector3 = generar_vector()

    # Construir la matriz con los tres vectores
    matrix = [vector1, vector2, vector3]

    # Imprimir los vectores generados
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Vector 3:", vector3)

    # Imprimir la matriz generada
    print("\nMatriz generada:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
