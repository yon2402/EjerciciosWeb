import random  # Importa el módulo random para generar números aleatorios

def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    return sum(notas) / len(notas) if notas else 0.0  # Suma las notas y las divide por la cantidad de notas. Si la lista está vacía, devuelve 0.0.

def main():
    NUM_STUDENTS = 25  # Define la cantidad de estudiantes
    NUM_NOTES = 4  # Define la cantidad de notas por estudiante

    estudiantes = []  # Lista para almacenar la información de los estudiantes
    
    for i in range(NUM_STUDENTS):  # Itera sobre el número de estudiantes
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")  # Solicita el nombre del estudiante
        apellido = input(f"Ingrese el apellido del estudiante {i + 1}: ")  # Solicita el apellido del estudiante

        # Genera 4 notas aleatorias entre 1 y 5 con dos decimales
        notas = [round(random.uniform(1, 5), 2) for _ in range(NUM_NOTES)]
        
        promedio = calcular_promedio(notas)  # Calcula el promedio de las notas

        # Agrega la información del estudiante como una tupla a la lista estudiantes
        estudiantes.append((nombre, apellido, notas, promedio))

    print("\n======== Notas de los estudiantes ========")
    
    # Recorre la lista de estudiantes y muestra su información
    for nombre, apellido, notas, promedio in estudiantes:
        # Convierte la lista de notas en una cadena formateada con dos decimales
        notas_str = ", ".join(f"{n:.2f}" for n in notas)  
        
        # Muestra los datos del estudiante
        print(f"Alumno: {nombre} {apellido} | Notas: {notas_str} | Promedio: {promedio:.2f}")

# Ejecuta la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()

