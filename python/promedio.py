#Jorge Collao
#Media Calcultor
#usernumfloat=[float(i) for i in usrnum]

def promedio():

    print('Ingrese los numeros separados por una coma')
    usrinput=input()
    usrnum=usrinput.split(",")
    usrnumfloat=[]

    for i in usrnum:
        usrnumfloat.append(float(i))
        
    suma=sum(usrnumfloat)
    prom =suma/len(usrnumfloat)
    
    print(usrnumfloat)
    print(prom)
promedio()

