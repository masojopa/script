#Jorge_Collao
#Larges Prime factor of a given digit

def factores(x):
    
    factor=[]
    for i in range(1,x+1):
        if x%i==0:
            factor.append(i)
    return(factor)

def primo(y):
    
    prim=[]
    for j in y:
        if len(factores(j))==2:
            prim.append(j)
    return(prim)


def main():

    lf = int(input("Ingrese un Numero para calcular sus factores Primos,\n"))
    print(primo(factores(lf)))

main()


