#Jorge_Collao
#Larges Prime number up to a given digit

def exponent():
    
    prime=[]
    primos=[]
    n=631
    for i in range(2,n+1):
        primos=True
        for j in range(2,int(n**0.5)+1):
            x=(i%j==0)
            if x:
               primos=False
               break 
        if primos:
            prime.append(i)
    print(prime)
exponent()
