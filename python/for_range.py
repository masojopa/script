#Jorge_Collao
#Exercise of the for loop with range()

def exponent():
    
    print('\n','Enter a')
    a=float(input())
    print('\n','Enter b')
    b=int(input())
    c=1.0
    for i in range(b):
        c=c*a
    print(c)

exponent()
