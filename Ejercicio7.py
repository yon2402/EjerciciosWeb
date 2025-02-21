def calculate_percent(cant, total_cant):
    return (cant / total_cant) * 100

def main():
    total = int(input("Cuantos estudiantes hay en el salon? "))
    
    men_total = int(input("Cuantos hombres hay: "))
    
    women_total = int(input("Cuantas mujeres hay: "))

    percent_men = calculate_percent(men_total, total)
    
    percent_women = calculate_percent(women_total, total)

    message = (
        f"El salon en total tiene: {total} estudiantes\n"
        f"De los cuales {men_total} son hombres\n"
        f"y {women_total} son mujeres\n"
        f"Representando respectivamente un {percent_men:.2f}% y un {percent_women:.2f}% del total"
    )

    print(message)

if __name__ == "__main__":
    main()