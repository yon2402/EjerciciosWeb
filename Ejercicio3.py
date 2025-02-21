def calculate_average(grades):
    """
    Calcula el promedio de una lista de calificaciones.
    
    Parámetros:
    - grades: Lista de números (float) que representan las calificaciones parciales.
    
    Retorna:
    - El promedio de las calificaciones. Si la lista está vacía, retorna 0.
    """
    total = sum(grades)  # Suma todas las calificaciones de la lista
    return total / len(grades) if grades else 0  # Divide el total por la cantidad de calificaciones


def calculate_weighted(value, weight):
    """
    Calcula la contribución ponderada de una calificación.
    
    Parámetros:
    - value: La calificación a ponderar.
    - weight: El porcentaje de ponderación (por ejemplo, 0.55 para 55%).
    
    Retorna:
    - El valor multiplicado por su porcentaje de ponderación.
    """
    return value * weight


def main():
    # Definición de los porcentajes de ponderación
    PERCENT_PARTIAL = 0.55      # 55% del promedio de las calificaciones parciales
    PERCENT_FINAL_EXAM = 0.30   # 30% de la calificación del examen final
    PERCENT_FINAL_WORK = 0.15   # 15% de la calificación del trabajo final

    # Crear una lista para almacenar las tres calificaciones parciales
    partial_grades = []
    
    # Solicitar al usuario ingresar las tres calificaciones parciales
    for i in range(3):
        grade = float(input(f"Digite la nota parcial número {i + 1} (del 0 al 5): "))
        partial_grades.append(grade)  # Se añade cada calificación a la lista

    # Solicitar la calificación del examen final
    final_exam_grade = float(input("Digite la nota de su examen final: "))
    # Solicitar la calificación del trabajo final
    final_work_grade = float(input("Digite la nota de su trabajo final: "))

    # Calcular el promedio de las tres calificaciones parciales
    average_partial = calculate_average(partial_grades)

    # Calcular la contribución ponderada de cada parte:
    weighted_partial = calculate_weighted(average_partial, PERCENT_PARTIAL)  # 55% del promedio parcial
    weighted_exam = calculate_weighted(final_exam_grade, PERCENT_FINAL_EXAM)  # 30% del examen final
    weighted_work = calculate_weighted(final_work_grade, PERCENT_FINAL_WORK)  # 15% del trabajo final

    # Sumar las contribuciones para obtener la calificación final
    final_grade = weighted_partial + weighted_exam + weighted_work

    # Preparar el mensaje final con formato, mostrando dos decimales para cada valor
    result = (
        f"El promedio de calificaciones parciales fue: {average_partial:.2f} con un 55% ponderación para un total de: {weighted_partial:.2f}\n"
        f"El 30% de su examen final es de: {weighted_exam:.2f}\n"
        f"El 15% de su trabajo final es de: {weighted_work:.2f}\n"
        f"Obteniendo una nota final de: {final_grade:.2f}"
    )

    # Imprimir el resultado final
    print(result)


# Se verifica si el script se está ejecutando directamente y se llama a la función principal
if __name__ == "__main__":
    main()
