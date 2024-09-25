#Fibonacci_Series_2
#Jorge_Collao

a,b,c = 0,1,0
d = [0]

while(a<500):
    #print(a,end = '+')
    a,b = b,a+b
    d.append(a)
    #print(d)
    c=c+a
print(d[0:(len(d)-1)])    
print('\n','Total ',c-a)
