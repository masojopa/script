#Jorge_Collao
#Euler 1
#List all natural numbers below "n" that are multiples  of 3 or 5

def multi():
    
    print('\n','List all natural numbers below "n" that                 are multiples  of 3 or 5')
    print('\n','Please enter "n"')
    suma=0
   # mul=[]
    n=int(input())
    for i in range(1,n):
        if ((i%3 == 0) or (i%5 == 0)):
            suma=suma+i
           # mul.appe6nd(i)
           # print(mul)
    print(suma)


multi()
