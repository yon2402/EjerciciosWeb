def calculate_percent(cant, total_cant):
    # Esta función calcula el porcentaje que representa 'cant' sobre 'total_cant'
    # Se realiza la división y se multiplica por 100 para obtener el porcentaje.
    return (cant / total_cant) * 100

def main():
    # Solicita al usuario ingresar la cantidad total de estudiantes en el salón
    # y convierte la entrada de tipo cadena a entero.
    total = int(input("Cuantos estudiantes hay en el salon? "))
    
    # Solicita al usuario ingresar la cantidad de hombres y lo convierte a entero.
    men_total = int(input("Cuantos hombres hay: "))
    
    # Solicita al usuario ingresar la cantidad de mujeres y lo convierte a entero.
    women_total = int(input("Cuantas mujeres hay: "))

    # Calcula el porcentaje de hombres usando la función 'calculate_percent'
    percent_men = calculate_percent(men_total, total)
    
    # Calcula el porcentaje de mujeres usando la misma función
    percent_women = calculate_percent(women_total, total)

    # Prepara un mensaje formateado con los datos obtenidos:
    # - Se muestra el total de estudiantes.
    # - Se muestran la cantidad de hombres y mujeres.
    # - Se muestran los porcentajes correspondientes, formateados a dos decimales.
    message = (
        f"El salon en total tiene: {total} estudiantes\n"
        f"De los cuales {men_total} son hombres\n"
        f"y {women_total} son mujeres\n"
        f"Representando respectivamente un {percent_men:.2f}% y un {percent_women:.2f}% del total"
    )

    # Imprime el mensaje final en la consola.
    print(message)

# Verifica si el script se está ejecutando directamente y, en ese caso, llama a la función 'main'
if __name__ == "__main__":
    main()
