#JorgeCollao
#Simple Match Statement

def runMatch():

    num = int(input('Enter a number between 1 and 3 '))

    # A match case
    match num :

        # Patern 1
        case 1:
            print("One")

        # Patern 2
        case 2:
            print("Two")

        # Patern 3
        case 3:
            print("Tree")

        # Default patern
        case other:
            print("Number is not between 1 and 3")


runMatch()
