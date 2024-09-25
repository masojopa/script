#Fibonacci_Series_4
#Jorge_Collao
#Returns the fibonacci series and its sum
#after a detrmined number of iterations
#It's a  continuations of Fibonacci_Series_4

start_stop = 'y'

while start_stop == 'y':
    a,b = 0,1
    total_sum = 0
    count = 0
    list_serie=[]

    print("Enter N° of Iterations")
    user_input = int(input())
    iterations = user_input-1

    while(count <= iterations):
        print (a,end = '+')
        total_sum = total_sum + a
        list_serie.append(total_sum)
        a,b = b,a+b
        count = count+1
    print('\n',list_serie)
    print('\n','Total ',total_sum)
    print('\n')
    print('Type -y- to continue, or -n-to stop','\n')
    start_stop = input()

