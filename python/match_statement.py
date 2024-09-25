#Jorge_Collao
#match_statement Excercise

# A Simple match case statement

def runmatch():
    num =int(input("Enter a number between 1 and 3: "))

    # match statement
    match num :

        # patern 1
        case 1:
            print("One")
        # patern 2
        case 2:
            print("Two")
        # patern 3
        case 3:
            print("Three")
        # default patern
        case _:
            print("Number not between 1 and 3")

runmatch()
