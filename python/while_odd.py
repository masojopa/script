#Jorge Collao
#Finding odd or wven number function

def odd_even():
    b='yes'
    while(b == 'yes'):
        print('Enter a number to see if is odd or even')
        a = int(input())
        if a%2 == 0:
            print('It is an even Number')
        else:
            print('It is an odd Number')
        print('To continue type yes')
        b = input()
    else:
        print('Thanks')
           # break

odd_even()

