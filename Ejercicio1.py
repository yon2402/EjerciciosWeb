def calculate_commission(sales):
    # Define el porcentaje de comisión
    PERCENTAGE_COMMISSION = 0.1
    # Calcula la comisión multiplicando las ventas por el porcentaje de comisión
    return sales * PERCENTAGE_COMMISSION

def calculate_gross_salary(base_salary, total_sales):
    # Calcula el sueldo bruto sumando el sueldo base y la comisión generada por las ventas
    return base_salary + calculate_commission(total_sales)

def calculate_net_salary(gross_salary):
    # Define el porcentaje de impuestos
    PERCENTAGE_TAXES = 0.19
    # Calcula el sueldo neto restando los impuestos al sueldo bruto
    return gross_salary - (gross_salary * PERCENTAGE_TAXES)

def main():
    # Solicita al usuario ingresar el sueldo base y lo convierte a flotante
    sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
    # Solicita al usuario ingresar el total de ventas y lo convierte a flotante
    total_ventas = float(input("Digite el total de ventas realizadas: "))

    # Calcula la comisión de ventas
    comision = calculate_commission(total_ventas)
    # Calcula el sueldo bruto
    sueldo_bruto = calculate_gross_salary(sueldo_base, total_ventas)
    # Calcula el sueldo neto después de impuestos
    sueldo_neto = calculate_net_salary(sueldo_bruto)

    # Formatea e imprime los resultados
    result = (f"\nSueldo base: {sueldo_base:.2f}\n"
              f"Total de ventas: {total_ventas:.2f}\n"
              f"Comisión de ventas (10%): {comision:.2f}\n"
              f"Sueldo Bruto: {sueldo_bruto:.2f}\n"
              f"Sueldo Neto: {sueldo_neto:.2f}")
    
    print(result)

# Verifica si el script se está ejecutando directamente y llama a la función principal
if __name__ == "__main__":
    main()
