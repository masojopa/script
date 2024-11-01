#Jorge_Collao
#Larges Prime number up to a given digit

def exponent():
    
    prime=[]
    primos=[]
    for i in range(1,20):
        for j in range(1,20):
            #print (i%j)
            if (i%j)==0:
                 prime.append(i)

        print(prime)
exponent()
