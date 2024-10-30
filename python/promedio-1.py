#Jorge Collao
#Media Calcultor
#usernumfloat=[float(i) for i in usrnum]

def promedio():
    print('\n')
    usrinput=input('Ingrese numeros para calcular el promedio separados por una coma \n')
    usrinput=usrinput.split(",")
    usrnumfloat=[]

    for i in usrinput:
        usrnumfloat.append(float(i))
        
    suma=sum(usrnumfloat)
    prom=suma/len(usrnumfloat)
    
    print('El promedio de los numeros ingresados es','\n',prom)
    print('\n')
promedio()

