import random  

def count_using_filter(lst, x):
    return sum(1 for num in filter(lambda num: num == x, lst))

def count_using_reduce(lst, x):
    from functools import reduce  
    return reduce(lambda count, num: count + 1 if num == x else count, lst, 0)

def count_using_map_reduce(lst, x):
    return sum(map(lambda num: 1 if num == x else 0, lst))

def main():
    size = int(input("Digite la cantidad del vector a generar: "))  
    numbers = [random.randint(0, 10) for _ in range(size)]  

    print("Vector generado:", numbers)  
    x = int(input("Digite el número a contar: "))  

    x_using_filter = count_using_filter(numbers, x)
    x_using_reduce = count_using_reduce(numbers, x)
    x_using_map = count_using_map_reduce(numbers, x)

    print(f"El número {x} fue encontrado:")
    print(f"{x_using_filter} veces usando Filter")
    print(f"{x_using_reduce} veces usando Reduce")
    print(f"{x_using_map} veces usando Map")

if __name__ == "__main__":
    main()