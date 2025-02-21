import random  

def generate_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def divide_list_by_two(lst):
    return [n / 2 for n in lst if n % 2 == 0]

def main():
    size = int(input("Ingrese el tamaño de la lista: "))  

    numbers = generate_list(size)  
    result = divide_list_by_two(numbers)  

    print("Lista original:", numbers)  
    print("\nLista transformada:", result)  

if __name__ == "__main__":
    main()