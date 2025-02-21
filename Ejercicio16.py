import random  # Importa el módulo random para generar números aleatorios

def count_using_filter(lst, x):
    """Cuenta cuántas veces aparece x en la lista usando filter."""
    return sum(1 for num in filter(lambda num: num == x, lst))
    # filter(lambda num: num == x, lst) filtra los elementos iguales a x en la lista.
    # sum(1 for num in ...) cuenta los elementos filtrados sumando 1 por cada coincidencia.

def count_using_reduce(lst, x):
    """Cuenta cuántas veces aparece x en la lista usando reduce."""
    from functools import reduce  # Importa reduce desde functools
    return reduce(lambda count, num: count + 1 if num == x else count, lst, 0)
    # reduce toma una función lambda que incrementa count en 1 si num == x, empezando desde 0.

def count_using_map_reduce(lst, x):
    """Cuenta cuántas veces aparece x en la lista usando map y sum."""
    return sum(map(lambda num: 1 if num == x else 0, lst))
    # map(lambda num: 1 if num == x else 0, lst) genera 1 si num == x y 0 en caso contrario.
    # sum(...) suma todos los valores generados, obteniendo la cantidad de veces que aparece x.

def main():
    size = int(input("Digite la cantidad del vector a generar: "))  # Pide al usuario el tamaño de la lista
    numbers = [random.randint(0, 10) for _ in range(size)]  # Genera una lista con números aleatorios entre 0 y 10

    print("Vector generado:", numbers)  # Muestra la lista generada
    x = int(input("Digite el número a contar: "))  # Pide al usuario el número a buscar

    # Llama a las funciones para contar cuántas veces aparece x en la lista
    x_using_filter = count_using_filter(numbers, x)
    x_using_reduce = count_using_reduce(numbers, x)
    x_using_map = count_using_map_reduce(numbers, x)

    # Imprime los resultados
    print(f"El número {x} fue encontrado:")
    print(f"{x_using_filter} veces usando Filter")
    print(f"{x_using_reduce} veces usando Reduce")
    print(f"{x_using_map} veces usando Map")

# Ejecuta la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
