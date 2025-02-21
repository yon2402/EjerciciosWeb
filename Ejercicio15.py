import random  

def calcular_promedio(notas):
   
    return sum(notas) / len(notas) if notas else 0.0  

def main():
    NUM_STUDENTS = 25  
    NUM_NOTES = 4  

    estudiantes = [] 
    
    for i in range(NUM_STUDENTS):  
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")  
        apellido = input(f"Ingrese el apellido del estudiante {i + 1}: ")  

        notas = [round(random.uniform(1, 5), 2) for _ in range(NUM_NOTES)]
        
        promedio = calcular_promedio(notas) 

        estudiantes.append((nombre, apellido, notas, promedio))

    print("\n======== Notas de los estudiantes ========")
    
    for nombre, apellido, notas, promedio in estudiantes:
        notas_str = ", ".join(f"{n:.2f}" for n in notas)  
        print(f"Alumno: {nombre} {apellido} | Notas: {notas_str} | Promedio: {promedio:.2f}")

if __name__ == "__main__":
    main()