# Jorge Collao 
# Average Calculator

def promedio():
    print("\n")
    print("Calculadora de Promedio")
    print("\n")
    
    while True:
        usrinput = input('Ingrese números separados por coma para calcular su promedio \n')
        usrinput = usrinput.split(",")
        
        try:
            usrnumfloat = [float(i) for i in usrinput]
            suma = sum(usrnumfloat)
            prom = suma / len(usrnumfloat)
            print('El promedio de los números ingresados es:', '\n', prom)
            print('\n')
            
            respuesta = input("Desea calcular otro promedio? (s/n) ")
            if respuesta.lower() != "s":
                break
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")

promedio()

