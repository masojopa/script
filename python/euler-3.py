#Jorge_Collao
#Larges Prime factot of a given digit

def factores(x):
    
    factor=[]
    i=1
    while i <= x:
        if x%i==0:
            factor.append(i)
        i=i+1    
    return(factor)

def main():
    y=int(input("Ingrese un Numero para calcular sus factores "))
    f=factores(y)
    print(f)

main()


