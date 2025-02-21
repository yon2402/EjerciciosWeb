def main():
    # Definir dimensiones de la matriz
    ROWS, COLS = 4, 5
    
    # Crear una matriz vacía
    matrix = []
    
    # Llenar la matriz con datos ingresados por el usuario
    for i in range(ROWS):
        row = []  # Lista temporal para almacenar cada fila
        for j in range(COLS):
            value = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)  # Agregar la fila a la matriz
    
    # Pedir al usuario el número que desea buscar
    target = int(input("Ingrese el número que desea buscar en la matriz: "))

    # Buscar la posición del número en la matriz
    position = None
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == target:
                position = (i, j)
                break
        if position:
            break

    # Imprimir la matriz ingresada
    print("Matriz ingresada:")
    for row in matrix:
        print(row)

    # Mostrar el resultado de la búsqueda
    if position:
        print(f"El número {target} se encuentra en la posición {position}")
    else:
        print("El número no se encuentra en la matriz")

# Ejecutar la función main
if __name__ == "__main__":
    main()
