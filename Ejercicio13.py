def main():
    ROWS, COLS = 4, 5
    
    matrix = []
    
    for i in range(ROWS):
        row = []  
        for j in range(COLS):
            value = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)  
    
    target = int(input("Ingrese el número que desea buscar en la matriz: "))

    position = None
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == target:
                position = (i, j)
                break
        if position:
            break

    print("Matriz ingresada:")
    for row in matrix:
        print(row)

    if position:
        print(f"El número {target} se encuentra en la posición {position}")
    else:
        print("El número no se encuentra en la matriz")

if __name__ == "__main__":
    main()