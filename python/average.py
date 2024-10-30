#Jorge Collao
#Average Calcultor

def promedio():
    print('\n')
    usrinput=input('Input numbers separeted by a coma to calculate it`s average \n')
    usrinput=usrinput.split(",")
    usrnumfloat=[]

    for i in usrinput:
        usrnumfloat.append(float(i))
        
    suma=sum(usrnumfloat)
    prom=suma/len(usrnumfloat)
    
    print('The mean of the input numbers is','\n',prom)
    print('\n')
promedio()

