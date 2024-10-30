#Jorge_Collao
#This code calculates the Fibonacci_Series and adds
#the even numbers 

a,b,d = 0,1,0
suma = 0
c=int(input('Please enter up to what value you whish to calculate,\n'))
while(a<c):
    if (a%2 == 0):
        suma=suma+a
        d+=1
    a,b = b,a+b
print('\n','The sum of all even numbers in the Fibonacci Series up to ',c,' is ',suma)
print ('\n','There are',d,'even numbers in the first',c,'digits of the Fibonacci Series')
