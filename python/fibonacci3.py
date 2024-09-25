#Fibonacci_Series_3
#Jorge_Collao
#Returns the fibonacci series and its sum
#after a detrmined number of iterations



a,b = 0,1
total_sum = 0
count = 0
list_serie=[]

print("Enter N° of Iterations")
iterations = (int(input())-1)

while(count <= iterations):
    print (a,end = '+')
    total_sum = total_sum + a
    list_serie.append(total_sum)
    a,b = b,a+b
    count = count+1
    if(iterations%2 == 0):
        print ('\n','Serie N° ',((iterations+1)//2),' ',        'Suma',list_serie[(int((iterations+1)//2))])
    elif(iterations%2 != 0):
        print ('\n','Serie N° ',(((iterations+1)//2)+1),        ' ','Suma',list_serie[(((iterations+1)//2)+1)]) 
print('\n',list_serie)
print('\n','Total ',total_sum)
#print ('\n','Serie N° ',((iterations+1)//2),' ','Suma',list_serie[(int((iterations+1)/2))])

  
