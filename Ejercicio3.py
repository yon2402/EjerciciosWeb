def calculate_average(grades):
    total = sum(grades)  
    return total / len(grades) if grades else 0  


def calculate_weighted(value, weight):
    return value * weight


def main():
    PERCENT_PARTIAL = 0.55      # 55% del promedio de las calificaciones parciales
    PERCENT_FINAL_EXAM = 0.30   # 30% de la calificación del examen final
    PERCENT_FINAL_WORK = 0.15   # 15% de la calificación del trabajo final

    partial_grades = []
    
    for i in range(3):
        grade = float(input(f"Digite la nota parcial número {i + 1} (del 0 al 5): "))
        partial_grades.append(grade)  # Se añade cada calificación a la lista

    final_exam_grade = float(input("Digite la nota de su examen final: "))
    final_work_grade = float(input("Digite la nota de su trabajo final: "))
    average_partial = calculate_average(partial_grades)

    weighted_partial = calculate_weighted(average_partial, PERCENT_PARTIAL)  # 55% del promedio parcial
    weighted_exam = calculate_weighted(final_exam_grade, PERCENT_FINAL_EXAM)  # 30% del examen final
    weighted_work = calculate_weighted(final_work_grade, PERCENT_FINAL_WORK)  # 15% del trabajo final

    final_grade = weighted_partial + weighted_exam + weighted_work

    result = (
        f"El promedio de calificaciones parciales fue: {average_partial:.2f} con un 55% ponderación para un total de: {weighted_partial:.2f}\n"
        f"El 30% de su examen final es de: {weighted_exam:.2f}\n"
        f"El 15% de su trabajo final es de: {weighted_work:.2f}\n"
        f"Obteniendo una nota final de: {final_grade:.2f}"
    )

    print(result)

if __name__ == "__main__":
    main()