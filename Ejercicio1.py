def calculate_commission(sales):
    PERCENTAGE_COMMISSION = 0.1
    return sales * PERCENTAGE_COMMISSION

def calculate_gross_salary(base_salary, total_sales):
    return base_salary + calculate_commission(total_sales)

def calculate_net_salary(gross_salary):
    PERCENTAGE_TAXES = 0.19
    return gross_salary - (gross_salary * PERCENTAGE_TAXES)

def main():
    sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
    total_ventas = float(input("Digite el total de ventas realizadas: "))

    comision = calculate_commission(total_ventas)
    sueldo_bruto = calculate_gross_salary(sueldo_base, total_ventas)
    sueldo_neto = calculate_net_salary(sueldo_bruto)

    result = (f"\nSueldo base: {sueldo_base:.2f}\n"
              f"Total de ventas: {total_ventas:.2f}\n"
              f"Comisión de ventas (10%): {comision:.2f}\n"
              f"Sueldo Bruto: {sueldo_bruto:.2f}\n"
              f"Sueldo Neto: {sueldo_neto:.2f}")
    
    print(result)

if __name__ == "__main__":
    main()