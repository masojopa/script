#Jorge_Collao
#This code calculates the Fibonacci_Series and adds
#the even numbers using a list[] and a for()

a,b = 0,1
listsum=[]
suma=0
c=int(input('Please enter up to what digit you whish to calculate,\n'))
while(a<c):
    if (a%2 == 0):
        listsum.append(a)
        for x in listsum:
            #suma=suma+listsum[x]
            suma=sum(listsum)
    a,b = b,a+b
print('\n','The sum of all even numbers in the Fibonacci Series up to ',c,' is ',suma)
#print(listsum)
#print('suma = ',suma)
