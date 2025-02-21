from datetime import date  

def main():
    year = int(input("Ingrese su año de nacimiento: "))
    
    month = int(input("Ingrese su mes de nacimiento (1-12): "))
    
    day = int(input("Ingrese su dia de nacimiento: "))

    birthdate = date(year, month, day)
    
    current_date = date.today()

    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    
    print(f"Su edad es de: {age} años")

if __name__ == "__main__":
    main()