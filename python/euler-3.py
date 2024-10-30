#Jorge_Collao
#Larges Prime number up to agiven digit

def exponent():
    
    x=int(input("Enter x,\n"))
    y=int((x//2)+1)
    prime=[]
    for i in range(1,x):
        for j in range(1,y):
            #print(i,j)
            a= (i%j)
            b= (i//j)
            if a==0 and b!=1 and b!=i:
                pass
            else:
                prime.append(i)
            print(prime)

exponent()
