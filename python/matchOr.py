#JorgeCollao
#Simple Match Statement

def runMatch():

    num = int(input('Enter a number between 1 and 6 '))

    # A match case
    match num :

        # Patern 1
        case 1|2:
            print("One or Two")

        # Patern 2
        case 3|4:
            print("Tree or Four")

        # Patern 3
        case 4|5:
            print("Five or Six")

        # Default patern
        case other:
            print("Number is not between 1 and 6")


runMatch()
