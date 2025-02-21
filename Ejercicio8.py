from datetime import date  # Importa la clase 'date' del módulo 'datetime' para trabajar con fechas

def main():
    # Solicita al usuario ingresar el año de nacimiento y lo convierte a entero
    year = int(input("Ingrese su año de nacimiento: "))
    
    # Solicita al usuario ingresar el mes de nacimiento (1-12) y lo convierte a entero
    month = int(input("Ingrese su mes de nacimiento (1-12): "))
    
    # Solicita al usuario ingresar el día de nacimiento y lo convierte a entero
    day = int(input("Ingrese su dia de nacimiento: "))

    # Crea un objeto 'date' que representa la fecha de nacimiento usando el año, mes y día ingresados
    birthdate = date(year, month, day)
    
    # Obtiene la fecha actual del sistema
    current_date = date.today()

    # Calcula la edad:
    # Se resta el año de nacimiento del año actual.
    # Además, se verifica si la fecha actual (mes y día) es anterior a la fecha de nacimiento (mes y día)
    # Esto significa que la persona aún no ha cumplido años en el año actual, por lo que se le resta 1.
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    
    # Imprime la edad calculada en la consola
    print(f"Su edad es de: {age} años")

# Verifica si el script se está ejecutando directamente y llama a la función 'main'
if __name__ == "__main__":
    main()
